import math


# LISTS AND TUPLES
def tuple_append(my_tuple, element):
    """Appends element to the end of my_tuple,
    returning the result as a new tuple."""
    # YOUR CODE HERE
    out = list(my_tuple)
    out.append(element)
    return tuple(out)


# PROBLEM 2
def list_diff(l1, l2):
    """The implementation takes 8 lines of code."""
    # YOUR CODE HERE
    li1 = list(l1)
    li2 = list(l2)
    for i in l1:
        for j in li2:
            print("i: " + i + " j: " + j)
            if i == j:
                li1.remove(i)
                li2.remove(i)
    return li1


# list_diff(['a', 'b', 'c', 'c', 'd'], ['b', 'a', 'a', 'c'])
# list_diff(['a', 'b', 'b', 'c'], ['b', 'c', 'd'])
# list_diff(['a', 'a', 'b', 'b', 'b'], ['a', 'a', 'b', 'b', 'c'])
# l1 = ['a', 'b', 'c', 'c', 'd']
# l2 = ['b', 'a', 'a', 'c']
# list_diff(l1, l2)


# DICTIONARIES AND SETS

def inverse(f):
    """Returns the dictionary that represents the inverse function of f.
        It can be solved in 8 lines."""
    # YOUR CODE HERE
    out = {}
    if len(set(f.values())) != len(list(f.values())):
        raise ValueError("lol")
    else:
        for i in range(len(list(f.values()))):
            out[list(f.values())[i]] = list(f.keys())[i]
    print(out)
    return out


# inverse({'a': 1, 'b': 3, 'c': 2})
# ANSWER: {1: 'a', 2: 'c', 3: 'b'}
inverse({'a': 2, 'b': 2})


# class Circle(object):
#
#     def __init__(self, x, y, r):
#         """Initializes a circle with center x, y and radius r."""
#         self.x = x
#         self.y = y
#         self.r = r
#
#     @property
#     def area(self):
#         """Returns the area of the circle.  This is defines as a property,
#         so you can call it on a circle c by doing c.area rather than c.area().
#         """
#         return math.pi * self.r * self.r
#
#     def contains(self, x, y):
#         """Returns true/false according to whether the circle contains the
#         (x, y) point or not."""
#         return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2
#
#
# c = Circle(3, 4, 5)
# print(c.area)
# print(c.contains(4, 5))
# print(c.contains(-2, 30))
