from math import erf
from numpy import array as vec
from numpy.linalg import norm as vec_size
from pandas import DataFrame


def approx(a, m, x):
    return ((a+x)**m-(a-x)**m)/((a+x)**m+(a-x)**m)

def quadratic_error(a, m, x):
    err = approx(a, m, x)-erf(x)
    return err**2

def average_quadratic_error(a, m):
    step = 0.1

    integral = integrate_quad_error(a, m, step)

    return integral/(a-step)

def integrate_quad_error(a, m, step):
    point = 0
    summ = 0

    while point < a-step:
        value = quadratic_error(a, m, point)
        df = quadratic_error(a, m, point+step)
        summ += value*step+0.5*df*step

        point += step

    return summ

def derive_2d(f, point, h):
    x = point[0]
    y = point[1]

    z = f(x, y)

    dx = f(x+h, y)-z
    dy = f(x, y+h)-z

    return vec((dx/h, dy/h))


def find_min_error_2d(start, max_iters):

    print(f"Start: {str(start)}")

    path = []

    gamma = 0.1 # Step size multiplier
    precision = 0.000001 # Desired precision of result 0.0000001 1e-7
    dx = 0.001 # 0.0000001

    current = start
    next = current

    for i in range(max_iters):

        if i % 10 == 0:
            print(f"{i}/{max_iters}")

        current = next
        next = current- gamma*derive_2d(average_quadratic_error, current, dx)

        err = average_quadratic_error(next[0], next[1])

        path.append((next[0], next[1], err))

        step = vec_size(next-current)

        if abs(step) <= precision:
            break

    return next, path

def main():
    start = (2.3, 2.5)
    max_iters = 2000

    point, path = find_min_error_2d(start, max_iters)

    df = DataFrame(path)
    df.to_csv(f"./data/algebraic_2d.csv", header=["a", "m", "error"], index = False)
    print(f"Closest point is {point}")

if __name__ == '__main__':
    main()
