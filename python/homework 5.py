from numbers import  Number
import random

def derivate(e, x):
    """Returns the derivative of e wrt x.
    It can be done in less than 15 lines of code."""
    if isinstance(e, str) and e != x or isinstance(e, Number):
        return 0
    elif isinstance(e, str) and e == x:
        return 1
    else:
        if isinstance(e, tuple):
            op, l, r = e
            if op in '+-':
                return op, derivate(l, x), derivate(r, x)
            elif op == '*':
                return '+', ('*', r, derivate(l, x)), ('*', l, derivate(r, x))
            else:
                return '/', ('-', ('*', r, derivate(l, x)), ('*', l, derivate(r, x))), ('*', r, r)


# Exercise: implementation of value equality
def variables(e, p=[]):
    if isinstance(e, tuple):
        _, l, r = e
        if isinstance(l, str):
            p.append(l)
        if isinstance(r, str):
            p.append(r)
        if isinstance(l, tuple):
            variables(l, p)
        if isinstance(r, tuple):
            variables(r, p)
    return set(p)


def value_equality(e1, e2, num_samples=1000, tolerance=1e-6):
    """Return True if the two expressions self and other are numerically
    equivalent.  Equivalence is tested by generating
    num_samples assignments, and checking that equality holds
    for all of them.  Equality is checked up to tolerance, that is,
    the values of the two expressions have to be closer than tolerance.
    It can be done in less than 10 lines of code."""
    # YOUR CODE HERE
    dank = 0
    for i in range(1000):
        if isinstance(e1, tuple) and isinstance(e2, tuple):
            op, l, r = e1




# print(derivate(('+', 'x', 'x'), 'x'))
# ('+', 1, 1)
# print(derivate(('-', 4, 'x'), 'x'))
# ('-', 0, 1)
# print(str(derivate(('*', 2, 'x'), 'x'))+" :mine")
# print("('+', ('*', 'x', 0), ('*', 2, 1)")
# print(derivate(('/', 2, 'x'), 'x'))
# print(('/', ('-', ('*', 'x', 0), ('*', 2, 1)), ('*', 'x', 'x')))

# e = ('*', ('+', 'x', 2), ('/', 'x', 'y'))
# print(variables(e))
# print({'x', 'y'})

### Tests for value equality

e1 = ('+', ('*', 'x', 1), ('*', 'y', 0))
e2 = 'x'
print(value_equality(e1, e2))
# true

e3 = ('/', ('*', 'x', 'x'), ('*', 'x', 1))
print(value_equality(e1, e3))
# true
e4 = ('/', 'y', 2)
print(value_equality(e1, e4))
# false
print(value_equality(e3, e4))
# false