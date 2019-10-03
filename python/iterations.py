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


# Simple RNG
def simple_random(seed = 0, n=10):
    i = seed
    r = []
    for _ in range(n):
        i = (i * 86753428563) % 94875394
        r.append(i / 94875394)
    return r
