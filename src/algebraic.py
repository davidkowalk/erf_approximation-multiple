import engine
from pandas import DataFrame
from math import e
from matplotlib import pyplot as plt

initial_values=[
(2,     2.24),
(2.25,  2.563),
(2.5,   2,874),
(2.75,  3.186),
(3,     3.495),
(3.25,  3.805),
(3.5,   4.112),
(3.75,  4.419),
(4,     4.725),
(4.25,  5.031),
(4.5,   5.336),
(4.75,  5.64),
(5,     5.945),
(5.25,  6.249),
(5.5,   6.552),
(5.75,  6.856),
(6,     7.159),
(6.25,  7.462),
(6.5,   7.766),
(6.75,  8.068),
(7,     8.371),
(7.25,  8.673),
(7.5,   8.979),
(7.75,  9.273),
(8,     9.580),
(8.25,  9.882),
(8.5,  10.184),
(8.75, 10.486),
(9,    10.787),
(9.25, 11.089),
(9.5,  11.391),
(9.75, 11.692),
(10,   11.994)
]

a = 2.2

def approx(m, x):
    return ((a+x)**m-(a-x)**m)/((a+x)**m+(a-x)**m)

def qerror(b, x):
    return engine.quad_error(approx, b, x)


def average_quadratic_error(b):
    return engine.integrate(qerror, b, 0, a-0.01, 0.01)/a


def graph_error(min, max, step):
    p = min
    data = []
    lowest = [min, 1]
    x = []
    y = []

    while p <= max:
        error = average_quadratic_error(p)
        data.append((p, error))
        x.append(p)
        y.append(error)
        p += step

        if error<lowest[1]:
            lowest = [p, error]

    #df = DataFrame(data)
    #df.to_csv(f"./graphs/algebraic{a}.csv", header=["b", "error"], index = False)
    print(f"Lowest: {lowest}")


    plt.plot(x, y)
    plt.show()


def find_min_error(start):
    print("Start: "+str(start))
    gamma = 0.1 # Step size multiplier
    precision = 0.000001 # Desired precision of result 0.0000001 1e-7
    max_iters = 5000 #200000
    dx = 0.0000001 # 0.0000001

    b, data = engine.gradient_descend(average_quadratic_error, start, precision, gamma, max_iters, dx)

    df = DataFrame(data)
    df.to_csv(f"./data/algebraic{a}.csv", header=["b", "error", "step"], index = False)


def main():
    global a

    #for set in initial_values:
    #    print(set)
    #    a=set[0]
    #    print("a: "+str(a))
    #    find_min_error(set[1])

    graph_error(2.4, 2.6, 0.001)


if __name__ == "__main__":
    main()
