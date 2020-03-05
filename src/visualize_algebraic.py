from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

#from matplotlib import cm
#from matplotlib.ticker import LinearLocator, FormatStrFormatter

from math import erf

def main():

    global dx
    print("Starting")

    pm = [] #m-achse

    a_min = 2
    a_max = 5

    m_min = 2
    m_max = 7

    mesh_density = 0.01

    dx = 0.1

    print("Setting up")
    X = np.arange(a_min, a_max, mesh_density)
    Y = np.arange(m_min, m_max, mesh_density)
    pa, pm = np.meshgrid(X, Y)

    print(f"Size: {pa.shape}")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #Generate data
    data = []
    error_a = []
    error_m = []
    error_z = []

    print("Generating Data")

    for im in range(len(pa)):
        Z = []

        for ia in range(len(pm[0])):
            point = get_average_quadratic_error(pa[im][ia], pm[im][ia])
            Z.append(point)


        data.append(Z)

    print("Generating Smallest Error")

    for ia in range(len(pm[0])):
        smallest_error = 1
        marker_a = 0
        marker_m = 0

        for im in range(len(pa)):

            #print(f"{ia}/{im}/")

            if data[im][ia] < smallest_error:
                smallest_error = data[im][ia]
                marker_a = pa[im][ia]
                marker_m = pm[im][ia]

        error_a.append(marker_a)
        error_m.append(marker_m)
        error_z.append(smallest_error)




    ax.set_xlabel('a')
    ax.set_ylabel('m')
    ax.set_zlabel('Average Error')

    print("Plotting Wireframe")
    #Plot a basic wireframe.
    data = np.array(data)
    print(f"Size: {data.shape}")
    ax.plot_wireframe(pa, pm, data, rstride=10, cstride=10)

    print("Plotting Minima")
    # Plot Minima
    error_a = np.array(error_a)
    error_m = np.array(error_m)
    error_z = np.array(error_z)
    ax.plot(error_a, error_m, error_z, label="Smallest Error", color="red")

    plt.show()

    contour(pa, pm, data)

def contour(pa, pm, data):

    print("Plotting Contour")
    plt.xlabel("alpha")
    plt.ylabel("m")

    #levels = [1e-5, 2e-5, 3e-5, 4e-5, 5e-5, 7e-5, 9e-5, 2e-4, 4e-4, 6e-4, 8e-4, 1e-3]

    print("1) Linear Color Distribution\n2) Logarithmic Color Distribution")
    mode = input("> ")

    if mode == "1":
        plt.pcolor(pa, pm, data, vmax=0.01)
    else:
        plt.pcolor(pa, pm, data, vmax=0.05, norm = LogNorm())

    plt.colorbar()

    plt.show()

def approximation(a, m, x):
    return ((a+x)**m-(a-x)**m)/((a+x)**m+(a-x)**m)

def error(a, m, x):
    return erf(x)-approximation(a, m, x)

def quad_error(a, m, x):
    err = error(a, m, x)
    return err*err

def integrate(func, a, m, start, end, dx):
    summ = 0
    point = start

    while point < end:
        func_value = func(a, m, point)
        df = func(a, m, point+dx)-func_value
        summ += func(a, m, point)*dx+0.5*dx*df

        point += dx

    return summ

def get_average_quadratic_error(a, m):
    return integrate(quad_error, a, m, 0, a-dx, dx)/a


if __name__ == "__main__":
    main()
