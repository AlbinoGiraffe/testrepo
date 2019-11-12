import math


class Expr(object):

    def __init__(self, *args):
        """Initializes an expression node, with a given list of children
        expressions."""
        self.children = args
        self.value = None  # The value of the expression.
        self.values = None  # The values of the child expressions.

    def __add__(self, other):
        """Constructs the sum of two expressions."""
        return Plus(self, other)

class Plus(Expr):
    pass

class V(Expr):
    """This class represents a variable.  The derivative rule corresponds
    to d/dx x = 1, but note that it will not be called, since the children
    of a variable are just numbers."""

    def assign(self, v):
        """Assigns a value to the variable."""
        self.children = [v]


class Expr(object):

    def __init__(self, *args):
        """Initializes an expression node, with a given list of children
        expressions."""
        self.children = args
        self.value = None  # The value of the expression.
        self.values = None  # The values of the child expressions.
        self.gradient = 0  # The value of the gradient.

    def op(self):
        """This operator must be implemented in subclasses; it should
        compute self.value from self.values, thus implementing the
        operator at the expression node."""
        raise NotImplementedError()

    def compute(self):
        """This method computes the value of the expression.
        It first computes the value of the children expressions,
        and then uses self.op to compute the value of the expression."""
        self.value = None  ### INSERT YOUR SOLUTION HERE
        return self.value

    def __repr__(self):
        return ("%s:%r %r (g: %r)" % (
            self.__class__.__name__, self.children, self.value, self.gradient))

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
    """This class represents a variable."""

    def assign(self, v):
        """Assigns a value to the variable.  Used to fit a model, so we
        can assign the various input values to the variable."""
        self.children = [v]

    def op(self):
        self.value = self.values[0]

    def __repr__(self):
        return "Variable: " + str(self.children[0])


class Plus(Expr):

    def op(self):
        self.value = self.values[0] + self.values[1]


class Multiply(Expr):

    def op(self):
        self.value = self.values[0] * self.values[1]


def expr_compute(self):
    """This method computes the value of the expression.
    It first computes the value of the children expressions,
    and then uses self.op to compute the value of the expression."""
    # YOUR CODE HERE
    self.values = []
    for k in self.children:
        if isinstance(k, Expr):
            self.values.append(expr_compute(k))
        else:
            self.values.append(k)
    self.op()
    return self.value


Expr.compute = expr_compute


class Multiply(Expr):
    """A multiplication expression."""

    def op(self):
        # YOUR CODE HERE
        self.value = self.values[0] * self.values[1]


def expr_derivate(self):
    """This method computes the derivative of the operator at the expression
    node.  It needs to be implemented in derived classes, such as Plus,
    Multiply, etc."""
    raise NotImplementedError()


Expr.derivate = expr_derivate


def expr_zero_gradient(self):
    """Sets the gradient to 0, recursively for this expression
    and all its children."""
    self.gradient = 0
    for e in self.children:
        if isinstance(e, Expr):
            e.zero_gradient()


Expr.zero_gradient = expr_zero_gradient


def expr_compute_gradient(self, de_loss_over_de_e=1):
    """Computes the gradient.
    de_loss_over_de_e is the gradient of the output.
    de_loss_over_de_e will be added to the gradient, and then
    we call for each child the method compute_gradient,
    with argument de_loss_over_de_e * d expression / d child.
    The value d expression / d child is computed by self.derivate. """
    pass  ### PLACEHOLDER FOR YOUR SOLUTION.


Expr.compute_gradient = expr_compute_gradient


class V(Expr):
    """This class represents a variable.  The derivative rule corresponds
    to d/dx x = 1, but note that it will not be called, since the children
    of a variable are just numbers."""

    def assign(self, v):
        """Assigns a value to the variable.  Used to fit a model, so we
        can assign the various input values to the variable."""
        self.children = [v]

    def op(self):
        self.value = self.values[0]

    def derivate(self):
        return [1.]  # This is not really used.


class Plus(Expr):
    """An addition expression.  The derivative rule corresponds to
    d/dx (x+y) = 1, d/dy (x+y) = 1"""

    def op(self):
        self.value = self.values[0] + self.values[1]

    def derivate(self):
        return [1., 1.]


class Multiply(Expr):
    """A multiplication expression. The derivative rule corresponds to
    d/dx (xy) = y, d/dy(xy) = x"""

    def op(self):
        self.value = self.values[0] * self.values[1]

    def derivate(self):
        return [self.values[1], self.values[0]]


def expr_compute_gradient(self, de_loss_over_de_e=1):
    """Computes the gradient.
    de_loss_over_de_e is the gradient of the output.
    de_loss_over_de_e will be added to the gradient, and then
    we call for each child the method compute_gradient,
    with argument de_loss_over_de_e * d expression / d child.
    The value d expression / d child is computed by self.derivate. """
    # YOUR CODE HERE
    self.compute()
    self.gradient += de_loss_over_de_e
    d = self.derivate()
    for k in self.children:
        if isinstance(k, Expr):
            k.compute_gradient(de_loss_over_de_e * d[self.children.index(k)])
    return self.gradient


Expr.compute_gradient = expr_compute_gradient


class Minus(Expr):
    """Operator for x - y"""

    def op(self):
        # YOUR CODE HERE
        self.value = self.values[0] - self.values[1]

    def derivate(self):
        # YOUR CODE HERE
        return [1.0, -1.0]


class Divide(Expr):
    """Operator for x / y"""

    def op(self):
        # YOUR CODE HERE
        self.value = self.values[0] / self.values[1]

    def derivate(self):
        # YOUR CODE HERE
        self.compute()

        return [1 / self.values[1],
                -self.values[0] / (self.values[1] * self.values[1])]


class Power(Expr):
    """Operator for x ** y"""

    def op(self):
        # YOUR CODE HERE
        self.value = pow(self.values[0], self.values[1])

    def derivate(self):
        # YOUR CODE HERE
        return [pow(self.values[0], self.values[1] - 1) * self.values[1],
                pow(self.values[0], self.values[1]) * math.log(self.values[0])]


class Negative(Expr):
    """Operator for -x"""

    def op(self):
        # YOUR CODE HERE
        self.value = -self.values[0]

    def derivate(self):
        # YOUR CODE HERE
        return [-1.]


points = [
    (-2, 2.7),
    (-1, 3),
    (0, 1.3),
    (1, 2.4),
    (3, 5.5),
    (4, 6.2),
    (5, 9.1),
]

va = V(0.)
vb = V(0.)
vc = V(0.)
vx = V(0.)
vy = V(0.)

# oy = va * vx * vx + vb * vx + vc
# loss = (vy - oy) * (vy - oy)


def fit(loss, points, params, delta=0.0001, num_iterations=4000):
    for iteration_idx in range(num_iterations):
        loss.zero_gradient()
        total_loss = 0.
        for x, y in points:
            vx.assign(x)
            vy.assign(y)
            loss.compute_gradient()
            total_loss += loss.value
        if (iteration_idx + 1) % 100 == 0:
            print("Loss:", total_loss)
        for vv in params:
            vv.assign(vv.value - delta * vv.gradient)
    return total_loss


# EXAMPLE 1
# lv = fit(loss, points, [va, vb, vc])
# print(lv)
# print("a:", va.value, "b:", vb.value, "c:", vc.value)

# EXAMPLE 2
# Parameters
# Sometimes you have to be careful about initial values.
# va = V(1.)
# vb = V(1.)

# x and y
# vx = V(0.)
# vy = V(0.)

# Predicted y
# oy = va * vx + vb

# Loss
# loss = (vy - oy) * (vy - oy)
# print(fit(loss, points, [va, vb]))

# Exercise: fit of y = a^x + bx + c

# vx = V(0.)
# vy = V(0.)
# va = V(1.)
# vb = V(0.)
# vc = V(0.)
# Define below what is oy and loss.
# oy = ...
# loss = ...
# YOUR CODE HERE
# oy = va ** vx + vb * vx + vc
# loss = (vy - oy) * (vy - oy)
# fit(loss, points, [va, vb, vc])

# Exercise: fit of y = a 2^x + b 2^{-x} + c x^3 + d x^2 + e x + f
vx = V(0.)
vy = V(0.)
va = V(1.)
vb = V(1.)
vc = V(0.)
vd = V(0.)
ve = V(0.)
vf = V(0.)
# Define here what is oy and what is the loss.
# oy = ...
# loss = ...
# YOUR CODE HERE
oy = va * 2 ** vx + vb * 2 ** -vx + vc * vx * vx * vx + vd * vx * vx + ve * vx + vf
loss = (vy - oy) * (vy - oy)
print(fit(loss, points, [va, vb, vc, vd, ve, vf], delta=0.000043, num_iterations=10000))
