from math import erf
from math import e

# For any function f(b, x) return the error between f and erf
def error(f, b, x):
    return erf(x)-f(b, x)

# For any function f(b, x) return the quadratic error between f and erf
def quad_error(f, b, x):
    err = error(f, b, x)
    return err*err

# Integrate any function between a start and an end point
def integrate(func, b, start, end, dx):
    summ = 0
    point = start

    while point < end:
        func_value = func(b, point)
        df = func(b, point+dx)-func_value
        summ += func(b, point)*dx+0.5*dx*df

        point += dx

    return summ


def derive(f, x, dx):
    return (f(x+dx)-f(x))/dx


def gradient_descend(f, start, precision, gamma, max_iters, dx):
    data = []

    next_x = start
    current_x = next_x

    for i in range(max_iters):

        if i % 10 == 0:
            print(f"{i}/{max_iters}")

        current_x = next_x
        next_x = current_x - gamma * derive(f, current_x, dx)

        step = next_x - current_x

        data.append((next_x, f(next_x), step))

        if abs(step) <= precision:
            break

    return next_x, data
