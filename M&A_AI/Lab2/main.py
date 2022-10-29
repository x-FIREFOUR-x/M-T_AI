import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import skfuzzy.fuzzymath as fuzzmath


#-------------------------------1---------------------------------
def triangle(x, a, b, c):
    f = fuzz.trimf(x, [a, b, c])
    plt.plot(x, f)
    plt.title(f"trimf(x,P) P=[{a}, {b}, {c}]")
    plt.show()

def gauss(x, z, G, name_f, index):
    f = fuzz.gaussmf(x, z, G)
    plt.plot(x, f)
    plt.title(f"gauss(x,P) P=[{z}, {G}]")

    plt.xlim(0, 0.1)
    plt.ylim(0)
    plt.xticks(np.arange(0, 1.1, step=0.1))
    plt.yticks(np.arange(0, 1.1, step=0.5))
    plt.grid(color='#CCCCCC', linestyle='-')

    plt.text(z, 1.025, name_f + str(index), fontsize=10)
    plt.plot([z], [1], 'o', zorder=2)

def membership_function(amount_function, G, name):
    x = np.arange(0, 1.02, 0.0025)
    step = 1 / (amount_function -1 )

    plt.figure(figsize=(14, 7))
    current_max_point = 0
    for i in range(1, amount_function + 1):
        gauss(x, current_max_point, G, name, i)
        current_max_point += step
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    membership_function(6, 0.0850, "mx")
    membership_function(6, 0.0850, "my")
    membership_function(9, 0.053, "mf")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
