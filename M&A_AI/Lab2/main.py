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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = np.arange(-10, 11, 0.25)
    triangle(x, -5, 0, 6)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
