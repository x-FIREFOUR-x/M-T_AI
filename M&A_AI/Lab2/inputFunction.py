import numpy as np
import matplotlib.pyplot as plt


def function_z(x, y):
    return x * np.cos(abs(y))

def view_input_function():
    x = np.linspace(0, 1, 30)
    y = np.linspace(0, 1, 30)

    X, Y = np.meshgrid(x, y)
    Z = function_z(X, Y)
    fig = plt.figure()
    plt.title("function for modeling: z = x * cos|y|")
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 100, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()