import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import skfuzzy.fuzzymath as fuzzmath
import math



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
    max_points = []
    for i in range(1, amount_function + 1):
        gauss(current_max_point, G, i)
        max_points.append(current_max_point)
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

def table_value_mf_for_mx_my(mx, my):
    table_values = []
    for i in range(0, len(my)):
        line_table = []
        for j in range(0, len(mx)):
            line_table.append(function_z(mx[j], my[i]))
        table_values.append(line_table)

    print()
    for line in table_values:
        for elem in line:
            print(f'{elem:.8f}', end='\t')
        print()

    return table_values

def table_name_mf_for_mx_my(table_value, mf):
    table = []
    for line in table_value:
        new_line = []
        for elem in line:
            name = ""
            min_sub = 1
            for i in range(0, len(mf)):
                if (abs(elem - mf[i]) < min_sub):
                    name = "mf" + str(i+1)
                    min_sub = abs(elem - mf[i])
            new_line.append(name)
        table.append(new_line)

    print()
    for line in table:
        for elem in line:
            print(elem, end='\t')
        print()

    return table



if __name__ == '__main__':
    mx = membership_function_gauss(6, 0.0850, "mx")
    my = membership_function_gauss(6, 0.0850, "my")
    mf = membership_function_gauss(9, 0.053, "mf")

    modeling_function()

    table = table_value_mf_for_mx_my(mx, my)
    table_name_mf_for_mx_my(table, mf)



