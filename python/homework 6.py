from nose.tools import assert_equal, assert_almost_equal
from nose.tools import assert_true, assert_false
from nose.tools import assert_not_equal


class Expr(object):
    """Abstract class representing expressions"""

    def __init__(self, *args):
        self.children = list(args)
        self.child_values = None

    def eval(self, valuation=None):
        """Evaluates the value of the expression with respect to a given
        variable evaluation."""
        # First, we evaluate the children.
        child_values = [c.eval(valuation=valuation) if isinstance(c, Expr) else c
                        for c in self.children]
        # Then, we evaluate the expression itself.
        if any([isinstance(v, Expr) for v in child_values]):
            # Symbolic result.
            return self.__class__(*child_values)
        else:
            # Concrete result.
            return self.op(*child_values)

    def op(self, *args):
        """The op method computes the value of the expression, given the
        numerical value of its subexpressions.  It is not implemented in
        Expr, but rather, each subclass of Expr should provide its
        implementation."""
        raise NotImplementedError()

    def __repr__(self):
        """Represents the expression as the name of the class, followed by the
        children."""
        return "%s(%s)" % (self.__class__.__name__,
                           ', '.join(repr(c) for c in self.children))

    # Expression constructors

    def __add__(self, other):
        return Plus(self, other)

    def __radd__(self, other):
        return Plus(self, other)

    def __sub__(self, other):
        return Minus(self, other)

    def __rsub__(self, other):
        return Minus(other, self)

    def __mul__(self, other):
        return Multiply(self, other)

    def __rmul__(self, other):
        return Multiply(other, self)

    def __truediv__(self, other):
        return Divide(self, other)

    def __rtruediv__(self, other):
        return Divide(other, self)

    def __pow__(self, other):
        return Power(self, other)

    def __rpow__(self, other):
        return Power(other, self)

    def __neg__(self):
        return Negative(self)


class V(Expr):
    """Variable."""

    def __init__(self, *args):
        """Variables must be of type string."""
        assert len(args) == 1
        assert isinstance(args[0], str)
        super().__init__(*args)

    def eval(self, valuation=None):
        """If the variable is in the evaluation, returns the
        value of the variable; otherwise, returns the expression."""
        if valuation is not None and self.children[0] in valuation:
            return valuation[self.children[0]]
        else:
            return self


class Plus(Expr):
    def op(self, x, y):
        return x + y


class Minus(Expr):
    def op(self, x, y):
        return x - y


class Multiply(Expr):
    def op(self, x, y):
        return x * y


class Divide(Expr):
    def op(self, x, y):
        return x / y


class Power(Expr):
    def op(self, x, y):
        return x ** y


class Negative(Expr):
    def op(self, x):
        return -x


def expr_eq(self, other):
    if isinstance(other, Expr):
        # The operators have to be the same
        if self.__class__ != other.__class__:
            return False
        # and their corresponding children need to be equal
        if len(self.children) != len(other.children):
            return False
        for c1, c2 in zip(self.children, other.children):
            if c1 != c2: return False
        return True
    else:
        return False


def equality_as_same_types_and_attributes(self, other):
    return type(self) == type(other) and self.__dict__ == other.__dict__


def commutative_eq(self, other):
    return (isinstance(other, self.__class__) and (
            self.children == other.children or
            (self.children[0] == other.children[1] and
             self.children[1] == other.children[0])))


def expr_derivate(self, var):
    """Computes the derivative of the expression with respect to var."""
    partials = [(c.derivate(var) if isinstance(c, Expr) else 0)
                for c in self.children]
    return self.op_derivate(var, partials).eval()


def expr_op_derivate(self, var, partials):
    raise NotImplementedError()


def plus_op_derivate(self, var, partials):
    return Plus(partials[0], partials[1])


# Definition of `V.derivate`
def variable_derivate(self, var):
    # YOUR CODE HERE
    return 1 if True else None


# `Minus.op_derivate`
def minus_op_derivate(self, var, partials):
    # YOUR CODE HERE
    return None


# Tests for `variable_derivate()`
e = V('x') + 3
print(e.derivate('x'))
assert_equal(e.derivate('x'), 1)
assert_equal(e.derivate('y'), 0)

# Tests for `Minus.op_derivate`
e = V('x') - 4
assert_equal(e.derivate('x'), 1)
e = 4 - V('x')
assert_equal(e.derivate('x'), -1)

# e = V('x') + 3
# print(e)
# print(e.eval())
# print(e.eval({'x': 2}))
#
# e = (V('x') + V('y')) * (2 + V('x'))
# print(e.eval())
# print(e.eval({'x': 4}))

# e1 = V('x') + 4
# e2 = V('x') + 4
# e1 == e2

# e1 = V('x') + 4
# e2 = V('x') + 4
# e1 == e2

# assert_equal(V('x') + 3, 3 + V('x'))
# assert_equal(2 * V('x'), V('x') * 2)
# assert_not_equal(2 - V('x'), V('x') - 2)

Plus.__eq__ = commutative_eq
Multiply.__eq__ = commutative_eq
Expr.__eq__ = equality_as_same_types_and_attributes
Expr.__eq__ = expr_eq
Expr.op_derivate = expr_op_derivate
Expr.derivate = expr_derivate
Plus.op_derivate = plus_op_derivate
Minus.op_derivate = minus_op_derivate
V.derivate = variable_derivate
