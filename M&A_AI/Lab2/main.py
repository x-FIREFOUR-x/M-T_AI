import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import skfuzzy.fuzzymath as fuzzmath
import math
from skfuzzy import control as ctrl



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


def function_z(x, y):
    return x * np.cos(abs(y))

def modeling_function():
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

def tables(mx, my, mf):
    def print_table(table, is_value):
        if is_value:
            sep = 8 * "_"
        else:
            sep = "_"

        print()
        print(4 * " ", end="")
        for i in range(1, len(table) + 1):
            print(sep + "mx" + str(i), end="")
        print()

        i = 1
        for line in table:
            print("my" + str(i), end="| ")
            for elem in line:
                if is_value:
                    print(f'{elem:.8f}', end=' ')
                else:
                    print(elem, end=' ')
            i += 1
            print()

    def print_mf():
        print()
        for i in range(1, len(mf)+1):
            print("__mf" + str(i), end="_")
        print()
        for i in range(1, len(mf)+1):
            print(f'{mf[i]:.3f}', end=" ")
        print()

    def table_value_mf_for_mx_my(mx, my):
        table_values = []
        for i in range(1, len(my)+1):
            line_table = []
            for j in range(1, len(mx)+1):
                line_table.append(function_z(mx[j], my[i]))
            table_values.append(line_table)

        print_table(table_values, True)
        return table_values

    def table_name_mf_for_mx_my(table_value, mf):
        table_name = []
        for line in table_value:
            new_line = []
            for elem in line:
                name = ""
                min_sub = 1
                for i in range(1, len(mf)+1):
                    if (abs(elem - mf[i]) < min_sub):
                        name = "mf" + str(i)
                        min_sub = abs(elem - mf[i])
                new_line.append(name)
            table_name.append(new_line)

        print_table(table_name, False)
        return table_name

    table = table_value_mf_for_mx_my(mx, my)
    print_mf()
    table_name_mf_for_mx_my(table, mf)



if __name__ == '__main__':
    mx = membership_function_gauss(6, 0.0850, "mx")
    my = membership_function_gauss(6, 0.0850, "my")
    mf = membership_function_gauss(9, 0.053, "mf")

    tables(mx, my, mf)
    modeling_function()





