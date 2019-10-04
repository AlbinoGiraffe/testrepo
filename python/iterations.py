def fib_fun(n=10):
    r = [0,1]
    # underscore means we don't care what the index is
    for _ in range(n-2):
        r.append(r[-1] + r[-2])
    return r


# list positions
l = [0, 1, 2, 3, 4, 5, 6]
i = 4
j = 5
print(l[i-j])


# Simple RN
def simple_random(seed = 0, n=10):
    i = seed
    r = []
    for _ in range(n):
        i = (i * 86753428563) % 94875394
        r.append(i / 94875394)
    return r


# Simple RNG
# "The yield statement suspends function’s
# execution and sends a value back to caller,
# but retains enough state to enable function to
# resume where it is left off"
# https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
def g_simple_random(seed=0):
    i = seed
    while True:
        i = ((i + 1)) * 86753428563 % 94875394
        yield i / 94875394


def addone(n, inc=None):
    # if None, assign value
    inc = inc or 1
    n += inc


def pass_student(name=None):
    name = name or "Luca"


# CONVENTION: default values of named parameters have to be constant
def gen_fibonacci(init_list=None):
    p = init_list or (0,1)
    assert len(p) > 1
    while True:
        n = p[-1] + p[-2]
        yield n
        p = p[-1:] + [n]


n = 0
for i in gen_fibonacci(init_list=[3,4]):
    print(i)
    n += 1
    if n > 10:
        break
