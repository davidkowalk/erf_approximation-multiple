import engine
from pandas import DataFrame
from math import e
from matplotlib import pyplot as plt

def approx(b, x):
    return 2 / (1+e**(-b*x))-1

def qerror(b, x):
    return engine.quad_error(approx, b, x)

def average_quadratic_error(b):
    return engine.integrate(qerror, b, 0, 5, 0.01)/5

def graph_error(min, max, step):
    p = min
    data = []
    x = []
    y = []

    while p <= max:
        error = average_quadratic_error(p)
        data.append((p, error))
        x.append(p)
        y.append(error)
        p += step

    plt.plot(x, y)
    plt.show()

    df = DataFrame(data)
    df.to_csv("./graphs/log.csv", header=["b", "error"], index = False)

def find_min_error():
    start = 2.404
    gamma = 0.1 # Step size multiplier
    precision = 0.00000001 # Desired precision of result 0.0000001
    max_iters = 2000 #200000
    dx = 0.0001 # 0.0000001

    b, data = engine.gradient_descend(average_quadratic_error, start, precision, gamma, max_iters, dx)

    df = DataFrame(data)
    df.to_csv("./data/log.csv", header=["b", "error", "step"], index = False)


def main():
    #find_min_error()
    graph_error(2.4, 2.41, 0.00001)



if __name__ == "__main__":
    main()
