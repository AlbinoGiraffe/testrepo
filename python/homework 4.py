class UndefinedSizeArray(Exception):
    pass


class SparseArrayDict(object):

    def __init__(self, *args, default=0., size=None):
        """If args are specified, they form the initial values for the array.
        Otherwise, we need to specify a size."""
        self.d = {}
        self.default = default
        if len(args) > 0:
            # We build a representation of the arguments args.
            self.length = len(args)
            for i, x in enumerate(args):
                if x != default:
                    self.d[i] = x
        if size is not None:
            self.length = size
        elif len(args) > 0:
            self.length = len(args)
        else:
            raise UndefinedSizeArray

    def __repr__(self):
        """We try to build a nice representation."""
        if len(self) <= 10:
            # The list() function uses the iterator, which is
            # defined below.
            return repr(list(self))
        else:
            s = "The array is a {}-long array of {},".format(
                self.length, self.default
            )
            s += " with the following exceptions:\n"
            ks = list(self.d.keys())
            ks.sort()
            s += "\n".join(["{}: {}".format(k, self.d[k]) for k in ks])
            return s

    def __setitem__(self, i, x):
        """This implements the a[3] = method"""
        assert isinstance(i, int) and i >= 0
        if x == self.default:
            # We simply remove any exceptions.
            if i in self.d:
                del self.d[i]
        else:
            self.d[i] = x
        # Adjusts the length.
        self.length = max(self.length, i - 1)

    def __getitem__(self, i):
        """This implements the a[]"""
        if i >= self.length:
            raise IndexError()
        return self.d.get(i, self.default)

    def __len__(self):
        return self.length

    def __iter__(self):
        # You may think this is a crazy way to iterate.
        # But in fact, it's quite efficient; there is no
        # markedly better way.
        for i in range(len(self)):
            yield self[i]

    def storage_len(self):
        """This returns a measure of the amount of space used for the array."""
        return len(self.d)


# Exercise: Implement add and sub for `SparseArrayDict`
# YOUR CODE HERE
def sparse_array_dict_add(self, other):
    b = len(self) if len(self) >= len(other) else len(other)
    ds = self.default
    dx = other.default
    x = 0
    o = SparseArrayDict(default=self.default, size=b)
    while x < b:
        for i in self:
            if i != ds:
                try:
                    if other[x] != dx:
                        o[x] = i + other[x]
                        x += 1
                    else:
                        o[x] = i + dx
                        x += 1
                except:
                    o[x] = i + dx
                    x += 1
            else:
                try:
                    if other[x] != dx:
                        o[x] = other[x] + ds
                        x += 1
                    else:
                        o[x] = ds + dx
                        x += 1
                except:
                    o[x] = ds + dx
                    x += 1
    return o


def sparse_array_dict_sub(self, other):
    b = len(self) if len(self) >= len(other) else len(other)
    ds = self.default
    dx = other.default
    x = 0
    o = SparseArrayDict(default=self.default, size=b)
    while x < b:
        for i in self:
            if i != ds:
                try:
                    if other[x] != dx:
                        o[x] = i - other[x]
                        x += 1
                    else:
                        o[x] = i - dx
                        x += 1
                except:
                    o[x] = i - dx
                    x += 1
            else:
                try:
                    if other[x] != dx:
                        o[x] = ds - other[x]
                        x += 1
                    else:
                        o[x] = ds - dx
                        x += 1
                except:
                    o[x] = ds - dx
                    x += 1
    return o


SparseArrayDict.__add__ = sparse_array_dict_add
SparseArrayDict.__sub__ = sparse_array_dict_sub

# Tests for arrays of the same length
# Let us test this with arrays of the same length first.
a = SparseArrayDict(1, 3, 4, 5)
b = SparseArrayDict(5, 4, 3, 2)
# c = a + b
# assert isinstance(c, SparseArrayDict)
# print(c[0], 6)
# print(c[1], 7)
# print(c[3], 7)
print(a.d.values())
