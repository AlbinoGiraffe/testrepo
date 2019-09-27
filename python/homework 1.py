import math

def list_diff(l1, l2):
    """The implementation takes 8 lines of code."""
    # YOUR CODE HERE
    li1 = list(l1)
    li2 = list(l2)
    print(li1)
    print(li2)
    print("__________________________")
    for i in l1:
        for j in l2:
            if i in li2:
                li1.remove(i)
                li2.remove(i)
            print(li1)
            print(li2)
            print("---------------------------")
    print(li1)
    # print(li0)
    # print(li1)
    # print(li2)
# if i not in li2:
#             li0.append(i)

# list_diff(['a', 'b', 'b', 'c'], ['b', 'c', 'd'])
# list_diff(['a', 'a', 'b', 'b', 'b'], ['a', 'a', 'b', 'b', 'c'])
#
# l1 = ['a', 'b', 'c', 'c', 'd']
# l2 = ['b', 'a', 'a', 'c']
# list_diff(l1, l2)


# list_diff(['a', 'b', 'c', 'c', 'd'], ['b', 'a', 'a', 'c'])


class Circle(object):

    def __init__(self, x, y, r):
        """Initializes a circle with center x, y and radius r."""
        self.x = x
        self.y = y
        self.r = r

    @property
    def area(self):
        """Returns the area of the circle.  This is defines as a property,
        so you can call it on a circle c by doing c.area rather than c.area().
        """
        return math.pi * self.r * self.r

    def contains(self, x, y):
        """Returns true/false according to whether the circle contains the
        (x, y) point or not."""
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2


c = Circle(3, 4, 5)
print(c.area)
print(c.contains(4, 5))
print(c.contains(-2, 30))
