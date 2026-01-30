import numpy as np

def trapezoid(f, a, b, n):
    h = (b - a) / n
    s = 0.0

    for i in range(1, n):
        x = a + i*h
        s += f(x)

    return h * ( (f(a) + f(b)) / 2 + s )

def simpson_13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even")

    h = (b - a) / n
    s1 = 0.0
    s2 = 0.0

    for i in range(1, n):
        x = a + i*h
        if i % 2 == 0:
            s2 += f(x)
        else:
            s1 += f(x)

    return (h/3) * (f(a) + f(b) + 4*s1 + 2*s2)

def simpson_38(f, a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be divisible by 3")

    h = (b - a) / n
    s3 = 0.0
    s2 = 0.0

    for i in range(1, n):
        x = a + i*h
        if i % 3 == 0:
            s2 += f(x)
        else:
            s3 += f(x)

    return (3*h/8) * (f(a) + f(b) + 3*s3 + 2*s2)

def boole(f, a, b, n):
    if n % 4 != 0:
        raise ValueError("n must be divisible by 4")

    h = (b - a) / n
    s = 0.0

    for i in range(0, n, 4):
        x0 = a + i*h
        s += (
            7*f(x0)
            + 32*f(x0 + h)
            + 12*f(x0 + 2*h)
            + 32*f(x0 + 3*h)
            + 7*f(x0 + 4*h)
        )

    return (2*h/45) * s


def weddle(f, a, b, n):
    if n % 6 != 0:
        raise ValueError("n must be divisible 6")

    h = (b - a) / n
    s = 0.0

    for i in range(0, n, 6):
        x0 = a + i*h
        s += (
            f(x0)
            + 5*f(x0 + h)
            + f(x0 + 2*h)
            + 6*f(x0 + 3*h)
            + f(x0 + 4*h)
            + 5*f(x0 + 5*h)
            + f(x0 + 6*h)
        )

    return (3*h/10) * s

f = lambda x: np.sin(x)
a = 0
b = np.pi
n = 24

print("Trapezoid:", trapezoid(f, a, b, n))
print("Simpson 1/3:", simpson_13(f, a, b, n))
print("Simpson 3/8:", simpson_38(f, a, b, n))
print("Boole:", boole(f, a, b, n))
print("Weddle:", weddle(f, a, b, n))