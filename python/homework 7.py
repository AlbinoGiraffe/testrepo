# Let us ensure that nose is installed.
from nose.tools import assert_equal, assert_true
from nose.tools import assert_false, assert_almost_equal
from nose.tools import assert_equal, assert_true
from nose.tools import assert_false, assert_almost_equal


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
"""The code for the `Plus` class, initially, is empty; no `Expr` methods are over-ridden."""
class Plus(Expr):
    """An addition expression."""

    pass
"""To construct expressions, we need one more thing.  So far, if we write things like `2 + 3`, 
Python will just consider these as expressions involving numbers, and compute their value.  
To write _symbolic_ expressions, we need symbols, or variables. 
A variable is a type of expression that just contains a value as child, 
and that has an `assign` method to assign a value to the variable.  
The `assign` method can be used to modify the variable's content (without `assign`,
 our variables would be constants!)."""
class V(Expr):
    """This class represents a variable.  The derivative rule corresponds
    to d/dx x = 1, but note that it will not be called, since the children
    of a variable are just numbers."""

    def assign(self, v):
        """Assigns a value to the variable."""
        self.children = [v]

"""This suffices for creating expressions.  Let's create one."""
# e = V(3) + 4
# e

"""## Computing the value of expressions

We now have our first expression.  To compute the expression value, we endow each expression with a method `op`,
whose task is to compute the value `self.value` of the expression from the list of values `self.values` of the children.

Let's implement the `compute` method for an expression.  This method will: 
1. Loop over the children, and computes the list `self.values` of children values as follows: 
    * If the child is an expression (an instance of `Expr`, obtain its value by calling `compute` on it. 
    * If the child is not an instance of `Expr`, then the child must be a number, and we can use its value directly. 
2. Call the method `op` of the expression, to compute `self.value` from `self.values`. 
3. return `self.value`. 

We will let you implement the `compute` method.  Hint: it takes just a couple of lines of code.
"""

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

"""Let us give `op` for `Plus`, `Multiply`, and for variables via `V`, so you can see how it works."""
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

"""Here you can write your implementation of the `compute` method."""
### Exercise: Implementation of `compute` method
def expr_compute(self):
    """This method computes the value of the expression.
    It first computes the value of the children expressions,
    and then uses self.op to compute the value of the expression."""
    # YOUR CODE HERE
    return self.value

Expr.compute = expr_compute

### Tests for compute
# First, an expression consisting only of one variable.
e = V(3)
assert_equal(e.compute(), 3)
assert_equal(e.value, 3)

# Then, an expression involving plus.
e = V(3) + 4
assert_equal(e.compute(), 7)
assert_equal(e.value, 7)

# And finally, a more complex expression.
e = (V(3) + 4) + V(2)
assert_equal(e.compute(), 9)
assert_equal(e.value, 9)

"""We will have you implement also multiplication."""
### Exercise: Implement `Multiply`

class Multiply(Expr):
    """A multiplication expression."""

    def op(self):
        return None
# YOUR CODE HERE

### Tests for `Multiply`
e = V(2) * 3
assert_equal(e.compute(), 6)

e = (V(2) + 3) * V(4)
assert_equal(e.compute(), 20)

"""## Implementing autogradient
The next step consists in implementing autogradient.  
Consider an expression $e = E(x_0, \ldots, x_n)$, 
computed as function of its children expressions $x_0, \ldots, x_n$.  

The goal of the autogradient computation is to accumulate, in each node of the expression, 
the gradient of the loss with respect to the node's value.  For instance, if the gradient is $2$, 
we know that if we increase the value of the expression by $\Delta$, 
then the value of the loss is increased by $2 \Delta$. 
We accumulate the gradient in the field `self.gradient` of the expression. 

We say _accumulate_ the gradient, because we don't really do:

    self.gradient = ...

Rather, we have a method `e.zero_gradient()` that sets all gradients to 0, and we then _add_ the gradient to this initial value of 0: 

    self.gradient += ... 

We will explain later in detail why we do so; for the moment, just accept it. 

### Computaton of the gradient

In the computation of the autogradient, the expression will receive as input the value $\partial L / \partial e$, where $L$ is the loss, and $e$ the value of the expression.  The quantity $\partial L / \partial e$ is the gradient of the loss with respect to the expression value. 

With this input, the method `compute_gradient` of Expr must do the following:

* It must _add_ $\partial L / \partial e$ to the gradient `self.gradient` of the expression. 
* It must compute for each child $x_i$ the partial derivative $\partial e / \partial x_i$, via a call to the method `derivate`.  The method `derivate` is implemented not for `Expr`, but for each specific operator, such as `Plus`, `Multiply`, etc: each operator knows how to compute the derivative with respect to its arguments.
* It must propagate to each child $x_i$ the gradient $\frac{\partial L}{\partial e} \cdot \frac{\partial e}{\partial x_i}$, by calling the method `compute_gradient` of the child with argument $\frac{\partial L}{\partial e} \cdot \frac{\partial e}{\partial x_i}$.
"""


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

"""Let us endow our operators `V`, `Plus`, `Multiply` with the `derivate` method, so you can see how it works in practice."""


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


"""Let us comment on some subtle points, before you get to work at implementing `compute_gradient`.  

**`zero_gradient`:** First, notice how in the implementation of `zero_gradient`, when we loop over the children, we check whether each children is an `Expr` via isinstance(e, Expr).  In general, we have to remember that children can be either `Expr`, or simply numbers, and of course numbers do not have methods such as `zero_gradient` or `compute_gradient` implemented for them. 

**`derivate`:** Second, notice how `derivate` is not implemented in `Expr` directly, but rather, only in the derived classes such as `Plus`.  The derivative of the expression with respect to its arguments depends on which function it is, obviously.  

For `Plus`, we have $e = x_0 + x_1$, and so: 

$$
\frac{\partial e}{\partial x_0} = 1 \qquad \frac{\partial e}{\partial x_1} = 1 \; ,
$$

because $d(x+y)/dx = 1$.  Hence, the `derivate` method of `Plus` returns

$$
\left[ \frac{\partial e}{\partial x_0}, \: \frac{\partial e}{\partial x_1}\right] \; = \; [1, 1] \; .
$$

For `Multiply`, we have $e = x_0 \cdot x_1$, and so:

$$
\frac{\partial e}{\partial x_0} = x_1 \qquad \frac{\partial e}{\partial x_1} = x_0 \; ,
$$

because $d(xy)/dx = y$.  Hence, the `derivate` method of `Plus` returns

$$
\left[ \frac{\partial e}{\partial x_0}, \: \frac{\partial e}{\partial x_1}\right] \; = \; [x_1, x_0] \; .
$$


**Calling `compute` before `compute_gradient`:** Lastly, a very important point: when calling `compute_gradient`, we will assume that `compute` has _already_ been called.  In this way, the value of the expression, and its children, are available for the computation of the gradient.  Note how in `Multiply.derivate` we use these values in order to compute the partial derivatives.

With these clarifications, we ask you to implement the `compute_gradient` method, which again must:

* _add_ $\partial L / \partial e$ to the gradient `self.gradient` of the expression; 
* compute $\frac{\partial e}{\partial x_i}$ for each child $x_i$ by calling the method `derivate` of itself; 
* propagate to each child $x_i$ the gradient $\frac{\partial L}{\partial e} \cdot \frac{\partial e}{\partial x_i}$, by calling the method `compute_gradient` of the child with argument $\frac{\partial L}{\partial e} \cdot \frac{\partial e}{\partial x_i}$.
"""


### Exercise: Implementation of `compute_gradient`

def expr_compute_gradient(self, de_loss_over_de_e=1):
    """Computes the gradient.
    de_loss_over_de_e is the gradient of the output.
    de_loss_over_de_e will be added to the gradient, and then
    we call for each child the method compute_gradient,
    with argument de_loss_over_de_e * d expression / d child.
    The value d expression / d child is computed by self.derivate. """
    # YOUR CODE HERE


Expr.compute_gradient = expr_compute_gradient

### Tests for `compute_gradient`

# First, the gradient of a sum.
# vx = V(3)
# vz = V(4)
# y = vx + vz
# assert_equal(y.compute(), 7)
# y.zero_gradient()
# y.compute_gradient()
# assert_equal(vx.gradient, 1.)

# Second, the gradient of a product.
# vx = V(3)
# vz = V(4)
# y = vx * vz
# assert_equal(y.compute(), 12)
# y.zero_gradient()
# y.compute_gradient()
# assert_equal(vx.gradient, 4)
# assert_equal(vz.gradient, 3)

# Finally, the gradient of the product of sums.

# vx = V(1)
# vw = V(3)
# vz = V(4)
# y = (vx + vw) * (vz + 3)
# assert_equal(y.compute(), 28)
# y.zero_gradient()
# y.compute_gradient()
# assert_equal(vx.gradient, 7)
# assert_equal(vz.gradient, 4)

"""## Why do we accumulate gradients?

We are now in the position of answering the question of why we accumulate gradients.  There are two reasons. 

### Multiple variable occurrence

The most important reason why we need to _add_ to the gradient of each node is that nodes, and in particular, variable nodes, can occur in multiple places in an expression tree.  To compute the total influence of the variable on the expression, we need to _sum_ the influence of each occurrence.  Let's see this with a simple example.  Consider the expression $y = x \cdot x$.  We can code it as follows:
"""

# vx = V(2.)  # Creates a variable vx and initializes it to 2.
# y = vx * vx

"""For $y = x^2$, we have $dy / dx = 2x = 4$, given that $x=2$.  How is this reflected in our code? 

Our code considers separately the left and right occurrences of `vx` in the expression; let us denote them with $vx_l$ and $vx_r$.  The expression can be written as $y = vx_l \cdot vx_r$, and we have that $\partial y / \partial \, vx_l = vx_r = 2$, as $vx_r = 2$.  Similarly, $\partial y / \partial \, vx_r = 2$.  These two gradients are added to `vx.gradient` by the method `compute_gradient`, and we get that the total gradient is 4, as desired.
"""

# y.compute()  # We have to call compute() before compute_gradient()
# y.zero_gradient()
# y.compute_gradient()
# print("gradient of vx:", vx.gradient)
# assert_equal(vx.gradient, 4)

"""### Multiple data to fit

The other reason why we need to tally up the gradient is that in general, we need to fit a function to more than one data point.  Assume that we are given a set of inputs $x_1, x_2, \ldots, x_n$ and desired outputs $y_1, y_2, \ldots, y_n$. Our goal is to approximate the desired ouputs via an expression $e(x, \theta)$ of the input, according to some parameters $\theta$.  Our goal is to choose the parameters $\theta$ to minimize the sum of the square errors for the points: 

$$
L_{tot}(\theta) = \sum_{i=1}^n L_i(\theta) \; ,
$$

where $L_i(\theta) = (e(x_i, \theta) - y_i)^2$ is the loss for a single data point.  The gradient $L_{tot}(\theta)$ with respect to $\theta$ can be computed by adding up the gradients for the individual points:

$$
\frac{\partial}{\partial \theta} L_{tot}(\theta) \;=\;
\sum_{i=1}^n \frac{\partial}{\partial \theta} L_i(\theta) \; .
$$

To translate this into code, we will build an expression $e(x, \theta)$ involving the input $x$ and the parameters $\theta$, and an expression 

$$
L = (e(x, \theta) - y)^2
$$

for the loss, involving $x, y$ and $\theta$.  We will then zero all gradients via `zero_gradient`. Once this is done, we compute the loss $L$ for each point, and then the gradient $\partial L / \partial \theta$ via a call to `compute_gradient`.  The gradients for all the points will be added, yielding the gradient for minimizing the total loss.

## Rounding up the implementation

Now that we have implemented autogradient, as well as the operators `Plus` and `Multiply`, it is time to implement the remaining operators: 

* `Minus`
* `Divide` (no need to worry about division by zero)
* `Power`, representing exponentiation (the `**` operator of Python)
* and the unary minus `Negative`.
"""

### Exercise: Implementation of `Minus`, `Divide`, `Power`, and `Negative`

import math


class Minus(Expr):
    """Operator for x - y"""

    def op(self):

    # YOUR CODE HERE

    def derivate(self):


# YOUR CODE HERE

class Divide(Expr):
    """Operator for x / y"""

    def op(self):

    # YOUR CODE HERE

    def derivate(self):


# YOUR CODE HERE

class Power(Expr):
    """Operator for x ** y"""

    def op(self):

    # YOUR CODE HERE

    def derivate(self):


# YOUR CODE HERE

class Negative(Expr):
    """Operator for -x"""

    def op(self):

    # YOUR CODE HERE

    def derivate(self):


# YOUR CODE HERE

"""Here are some tests."""

### Tests for `Minus`

# Minus.
# vx = V(3)
# vy = V(2)
# e = vx - vy
# assert_equal(e.compute(), 1.)
# e.zero_gradient()
# e.compute_gradient()
# assert_equal(vx.gradient, 1)
# assert_equal(vy.gradient, -1)

### Tests for `Divide`

from nose.tools import assert_almost_equal

# Divide.
# vx = V(6)
# vy = V(2)
# e = vx / vy
# assert_equal(e.compute(), 3.)
# e.zero_gradient()
# e.compute_gradient()
# assert_equal(vx.gradient, 0.5)
# assert_equal(vy.gradient, -1.5)

### Tests for `Power`

from nose.tools import assert_almost_equal

# Power.
# vx = V(2)
# vy = V(3)
# e = vx ** vy
# assert_equal(e.compute(), 8.)
# e.zero_gradient()
# e.compute_gradient()
# assert_equal(vx.gradient, 12.)
# assert_almost_equal(vy.gradient, math.log(2.) * 8., places=4)

### Tests for `Negative`

from nose.tools import assert_almost_equal

# Negative
# vx = V(6)
# e = - vx
# assert_equal(e.compute(), -6.)
# e.zero_gradient()
# e.compute_gradient()
# assert_equal(vx.gradient, -1.)

"""## Optimization

Let us use our ML framework to fit a parabola to a given set of points.  Here is our set of points:
"""

# points = [
#     (-2, 2.7),
#     (-1, 3),
#     (0, 1.3),
#     (1, 2.4),
#     (3, 5.5),
#     (4, 6.2),
#     (5, 9.1),
# ]

"""Let us display these points."""

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['figure.figsize'] = (8.0, 3.)
params = {'legend.fontsize': 'large',
          'axes.labelsize': 'large',
          'axes.titlesize': 'large',
          'xtick.labelsize': 'large',
          'ytick.labelsize': 'large'}
matplotlib.rcParams.update(params)


def plot_points(points):
    fig, ax = plt.subplots()
    xs, ys = zip(*points)
    ax.plot(xs, ys, 'r+')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


plot_points(points)

"""To fit a parabola to these points, we will build an `Expr` that represents the equation $\hat{y} = ax^2 + bx + c$, where $\hat{y}$ is the value of $y$ predicted by our parabola. 
If $\hat{y}$ is the predicted value, and $y$ is the observed value, to obtain a better prediction of the observations, we minimize the loss $L = (\hat{y} - y)^2$, that is, the square prediction error. 
Written out in detail, our loss is:

$$
    L \;=\; \left( y - \hat{y}\right)^ 2 \;=\; \left( y - (ax^2 + bx + c) \right)^2 \; .
$$

Here, $a, b, c$ are parameters that we need to tune to minimize the loss, and obtain a good fit between the parabola and the points. 
This tuning, or training, is done by repeating the following process many times:

* Zero the gradient
* For each point:
    * Set the values of x, y to the value of the point.
    * Compute the expression giving the loss.
    * Backpropagate.  This computes all gradients with respect to the loss, and in particular, the gradients of the coefficients $a, b, c$. 
* Update the coefficients $a, b, c$ by taking a small step in the direction of the negative gradient (negative, so that the loss decreases).
"""

va = V(0.)
vb = V(0.)
vc = V(0.)
vx = V(0.)
vy = V(0.)

oy = va * vx * vx + vb * vx + vc

loss = (vy - oy) * (vy - oy)

"""Below, implement the "for each point" part of the above informal description.  Hint: this takes about 4-5 lines of code."""


def fit(loss, points, params, delta=0.0001, num_iterations=4000):
    for iteration_idx in range(num_iterations):
        loss.zero_gradient()
        total_loss = 0.
        for x, y in points:
            ### You need to implement here the computaton of the
            ### loss gradient for the point (x, y).
            total_loss += loss.value
        if (iteration_idx + 1) % 100 == 0:
            print("Loss:", total_loss)
        for vv in params:
            vv.assign(vv.value - delta * vv.gradient)
    return total_loss


### Exercise: Implementation of `fit`

def fit(loss, points, params, delta=0.0001, num_iterations=4000):
    for iteration_idx in range(num_iterations):
        loss.zero_gradient()
        total_loss = 0.
        for x, y in points:
            # YOUR CODE HERE
            total_loss += loss.value
        if (iteration_idx + 1) % 100 == 0:
            print("Loss:", total_loss)
        for vv in params:
            vv.assign(vv.value - delta * vv.gradient)
    return total_loss


"""Let's train the coefficients `va`, `vb`, `vc`:"""

from nose.tools import assert_less

lv = fit(loss, points, [va, vb, vc])
assert_less(lv, 2.5)

"""Let's display the parameter values after the training:"""

print("a:", va.value, "b:", vb.value, "c:", vc.value)

"""Let's display the points, along with the fitted parabola."""

import numpy as np


def plot_points_and_y(points, vx, oy):
    fig, ax = plt.subplots()
    xs, ys = zip(*points)
    ax.plot(xs, ys, 'r+')
    x_min, x_max = np.min(xs), np.max(xs)
    step = (x_max - x_min) / 100
    x_list = list(np.arange(x_min, x_max + step, step))
    y_list = []
    for x in x_list:
        vx.assign(x)
        oy.compute()
        y_list.append(oy.value)
    ax.plot(x_list, y_list)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


plot_points_and_y(points, vx, oy)

"""This looks like a good fit!

Note that if we chose too large a learning step, we would not converge to a solution.  A large step causes the parameter values to zoom all over the place, possibly missing by large amounts the (local) minima where you want to converge.  In the limit where the step size goes to 0, and the number of steps to infinity, you are guaranteed (if the function is differentiable, and some other hypotheses) converge to the minimum; the problem is that it would take infinitely long.  You will learn in a more in-depth ML class how to tune the step size.
"""

# Let us reinitialize the variables.
va.assign(0)
vb.assign(0)
vc.assign(0)
# ... and let's use a big step size.
fit(loss, points, [va, vb, vc], delta=0.01, num_iterations=1000)

"""A step size of 0.01 was enough to take us to infinity and beyond.

Let us now show you how to fit a simple linear regression: $y = ax + b$, so $L = (y - (ax + b))^2$.
"""

# Parameters
# Sometimes you have to be careful about initial values.
va = V(1.)
vb = V(1.)

# x and y
vx = V(0.)
vy = V(0.)

# Predicted y
oy = va * vx + vb

# Loss
loss = (vy - oy) * (vy - oy)

fit(loss, points, [va, vb])

plot_points_and_y(points, vx, oy)

"""## Exercises

Using the method illustrated above, fit the following equations to our set of points.  Use `vx`, `xy` for $x$, $y$, and `va`, `vb`, `vc`, etc for the parameters.  This is important, or the tests won't pass.

$$
y = a^x + bx + c
$$
"""

### Exercise: fit of y = a^x + bx + c

vx = V(0.)
vy = V(0.)
va = V(1.)
vb = V(0.)
vc = V(0.)
# Define below what is oy and loss.
# oy = ...
# loss = ...
# YOUR CODE HERE
fit(loss, points, [va, vb, vc])

### Tests for convergence of fit of y = a^x + bx + c

"""Now, fit: 

$$
y = a \cdot 2^x + b \cdot 2^{-x} + c x^3 + d x^2 + e x + f
$$

Use a small enough step size, and a sufficient number of iterations, to obtain a final loss of no more than 2.5.

Hint: write `vx * vx * vx`, not `vx ** 3`, etc, since as currently written, the `**` operator cannot handle a negative basis.
"""

### Exercise: fit of y = a 2^x + b 2^{-x} + c x^3 + d x^2 + e x + f
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
fit(loss, points, [va, vb, vc, vd, ve, vf], delta=0.00002, num_iterations=10000)

### Tests for fit of  y = a 2^x + b 2^{-x} + c x^3 + d x^2 + e x + f

plot_points_and_y(points, vx, oy)