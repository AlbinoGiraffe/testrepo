from numbers import Number
import random


def compute(e, varval={}):
    if isinstance(e, Number):
        return e
    elif isinstance(e, str):
        v = varval.get(e)
        # If we find a value for e, we return it; otherwise we return e.
        return e if v is None else v
    else:
        op, l, r = e
        # We simplify the left and right subexpressions first.
        ll = compute(l, varval=varval)
        rr = compute(r, varval=varval)
        # And we carry out the operation if we can.
        if isinstance(ll, Number) and isinstance(rr, Number):
            if op == '+':
                return ll + rr
            elif op == '-':
                return ll - rr
            elif op == '*':
                return ll * rr
            elif op == '/' and rr != 0:
                return ll / rr
        # Not simplifiable.
        return op, ll, rr


def variable_substitution(e, d):
    """Performs variable substitutions in e according to the replacement dictionary d"""
    if isinstance(e, tuple):
        op, e1, e2 = e
        ee1 = variable_substitution(e1, d)
        ee2 = variable_substitution(e2, d)
        return op, ee1, ee2
    elif isinstance(e, Number):
        return e
    else:
        # We perform the substitution, if one is specified.
        return d.get(e, e)


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
    x = p
    if isinstance(e, str):
        return {e}
    elif isinstance(e, tuple):
        _, l, r = e
        if isinstance(l, str):
            x.append(l)
        if isinstance(r, str):
            x.append(r)
        if isinstance(l, tuple):
            variables(l, x)
        if isinstance(r, tuple):
            variables(r, x)
    return set(x)


# Exercise: implementation of value equality
def value_equality(e1, e2, num_samples=1000, tolerance=1e-6):
    """Return True if the two expressions self and other are numerically
    equivalent.  Equivalence is tested by generating
    num_samples assignments, and checking that equality holds
    for all of them.  Equality is checked up to tolerance, that is,
    the values of the two expressions have to be closer than tolerance.
    It can be done in less than 10 lines of code."""
    # YOUR CODE HERE
    for i in range(num_samples):
        r = random.gauss(0, 1)
        var1 = {element: r for element in variables(e1)}
        var2 = {element: r for element in variables(e2)}
        if abs(compute(e1, var1) - compute(e2, var2)) > tolerance: return False
    return True


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

# Tests for value equality

e1 = ('+', ('*', 'x', 1), ('*', 'y', 0))
# e2 = 'x'
# print(value_equality(e1, e2))
# true
# print(variables(e1))
# print(variables(e2))

e3 = ('/', ('*', 'x', 'x'), ('*', 'x', 1))
print(value_equality(e1, e3))
# print(variables(e1))
# print(variables(e3))
# # true
# e4 = ('/', 'y', 2)
# print(value_equality(e1, e4))
# false
# print(value_equality(e3, e4))
# false

