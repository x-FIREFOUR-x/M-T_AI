import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

from inputFunction import function_z

def triangle(x, a, b, c):
    f = fuzz.trimf(x, [a, b, c])
    plt.plot(x, f)
    plt.title(f"trimf(x,P) P=[{a}, {b}, {c}]")
    plt.show()


def membership_function_gauss(amount_function, G, name):
    def gauss(z, G, index):
        f = fuzz.gaussmf(x, z, G)
        plt.plot(x, f)

        plt.xlim(0, 0.1)
        plt.ylim(0)
        plt.xticks(np.arange(0, 1.1, step=0.1))
        plt.yticks(np.arange(0, 1.1, step=0.5))
        plt.grid(color='#CCCCCC', linestyle='-')

        plt.text(z, 1.025, name + str(index), fontsize=10)
        plt.plot([z], [1], 'o', zorder=2)

    x = np.arange(0, 1.02, 0.0025)
    step = 1 / (amount_function -1)

    plt.figure(figsize=(14, 7))
    current_max_point = 0
    max_points = {}
    for i in range(1, amount_function + 1):
        gauss(current_max_point, G, i)
        max_points[i] = current_max_point
        current_max_point += step
    plt.title(f"Membership function {name}")
    plt.show()
    return max_points

