import math

class CountingQueue(object):

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return repr(self.queue)

    def add(self, x, count=1):
        # If the element is the same as the last element, we simply
        # increment the count.  This assumes we can test equality of
        # elements.
        if len(self.queue) > 0:
            xx, cc = self.queue[-1]
            if xx == x:
                self.queue[-1] = (xx, cc + count)
            else:
                self.queue.append((x, count))
        else:
            self.queue = [(x, count)]

    def get(self):
        if len(self.queue) == 0:
            return None
        x, c = self.queue[0]
        if c == 1:
            self.queue.pop(0)
            return x
        else:
            self.queue[0] = (x, c - 1)
            return x

    def isempty(self):
        # Since the count of an element is never 0, we can just check
        # whether the queue is empty.
        return len(self.queue) == 0

# q = CountingQueue()
# q.add('a')
# print(q)
# q.add('b', count=5)
# print(q)
# q.add('c', count=2)
# print(q)
# while not q.isempty():
#     print(q.get())
#     print(q)


# Exercise: implement `__len__` for a counting queue
def countingqueue_len(self):
    """Returns the number of elements in the queue."""
    # YOUR CODE HERE
    o = 0
    print(q)
    for _, x in self.queue:
        o += x
    print(o)
    return o


# This is a way to add a method to a class once the class
# has already been defined.
CountingQueue.__len__ = countingqueue_len


# Exercise: Write an iterator for CountingQueue
# Note: it can be done elegantly in 3 lines of code.

def countingqueue_iter(self):
    """Iterates through all the elements of the queue,
    without removing them."""
    # YOUR CODE HERE
    for i, x in self.queue:
        for p in range(x, 0, -1):
            yield i


CountingQueue.__iter__ = countingqueue_iter

# q = CountingQueue()
# for i in range(10):
#     q.add('a')
# q.add('b')
# for i in range(3):
#     q.add('c', count=2)
# l1 = [x for x in q]
# l2 = []
# while not q.isempty():
#     l2.append(q.get())
# print(l1)
# print(l2)

# Tests for `CountingQueue.__iter__`
# q = CountingQueue()
# for i in range(10):
#     q.add('a')
# q.add('b')
# for i in range(3):
#     q.add('c', count=2)
# l1 = [x for x in q]
# l2 = []
# while not q.isempty():
#     l2.append(q.get())
# q = CountingQueue()
# for i in range(10):
#     q.add('a')
# q.add('b')
# for i in range(3):
#     q.add('c', count=2)
# print("Length: "+str(len(q)))

# Exercise: implement a prime number generator

# My solution is simple and not particularly optimized,
# and it is 12 lines long.


def prime_number_generator():
    """This generator returns all prime numbers."""
    # YOUR CODE HERE
    p = 0
    v = False
    while True:
        p += 1
        for i in range(2, p):
            # print("i: "+str(i)+" p: "+str(p))
            if p % i == 0:
                v = False
                break
            else:
                # print("lol")
                v = True
        if v:
            print(p)
            yield p


# i = 0
# for n in prime_number_generator():
#     # print(n)
#     i += 1
#     if i == 10:
#         break

# for n in prime_number_generator():
#     if n == 33:
#         raise Exception()
#     elif n == 37:
#         break

# Exercise: implement the `subsets` function for sets
def subsets(s):
    """Given a set s, yield all the subsets of s,
    including s itself and the empty set."""
    # YOUR CODE HERE
    # Got the idea from https://coderbyte.com/algorithm/print-all-subsets-given-set
    # total num of sets
    set_num = int(pow(2, len(s)))
    # convert set to list for easy indexing
    m = list(s)

    for i in range(0, set_num):
        # new list to yield
        k = []

        # convert to binary so that a 1=add, 0=ignore
        t = "{0:b}".format(i)

        # pad it according to length of set
        while len(t) < len(s):
            t = '0' + t

        # iterate over binary to match 1's
        for j in range(0, len(t)):
            if t[j] == '1':
                k.append(m[j])
        yield k





# Tests for `subsets`
s = set([1, 2, 3])
for t in subsets(s):
    print(t)
# print(len(list(subsets(s))))