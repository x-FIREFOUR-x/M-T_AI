import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz

def print_function(x, f, max_point, number_func, name_func):
    plt.plot(x, f)

    plt.xlim(0, 0.1)
    plt.ylim(0)
    plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.yticks(np.arange(0, 1.1, step=0.5))
    plt.grid(color='#CCCCCC', linestyle='-')

    plt.text(max_point, 1.025, name_func + str(number_func), fontsize=10)
    plt.plot([max_point], [1], 'o', zorder=2)


def membership_function_gauss(amount_function, G, name_func):
    def gauss(z, G, number_func):
        f = fuzz.gaussmf(x, z, G)
        print_function(x, f, z, number_func, name_func)

    x = np.arange(0, 1.02, 0.0025)
    step = 1 / (amount_function -1)

    plt.figure(figsize=(14, 7))
    current_max_point = 0
    max_points = {}
    for i in range(1, amount_function + 1):
        gauss(current_max_point, G, i)
        max_points[i] = current_max_point
        current_max_point += step
    plt.title(f"Membership function {name_func}")
    plt.show()

    return max_points


def membership_function_triangle(amount_function, name_func):
    def triangle(a, b, c, number_func):
        f = fuzz.trimf(x, [a, b, c])
        print_function(x, f, b, number_func, name_func)

    x = np.arange(0, 1.02, 0.0025)
    step = 1 / (amount_function - 1)

    plt.figure(figsize=(14, 7))
    current_max_point = 0
    max_points = {}
    for i in range(1, amount_function + 1):
        triangle(current_max_point - step, current_max_point, current_max_point + step, i)
        max_points[i] = current_max_point
        current_max_point += step
    plt.title(f"Membership function {name_func}")
    plt.show()

    return max_points


def membership_function_trapation(amount_function, name_func):
    def triangle(a, b, c, d, number_func):
        f = fuzz.trapmf(x, [a, b, c, d])
        print_function(x, f, b, number_func, name_func)

    x = np.arange(0, 1.02, 0.0025)
    step = 1 / (amount_function - 1)

    plt.figure(figsize=(14, 7))
    current_max_point = 0
    max_points = {}
    for i in range(1, amount_function + 1):
        triangle(current_max_point - step, current_max_point, current_max_point + step / 2, current_max_point + step, i)
        max_points[i] = current_max_point
        current_max_point += step
    plt.title(f"Membership function {name_func}")
    plt.show()

    return max_points