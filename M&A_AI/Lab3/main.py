import numpy as np
import random as rand
import matplotlib.pyplot as plt
import skfuzzy as fuzz


def random_generate_points(amount, min_limit, max_limit):
    points = []
    for i in range(0, amount):
        points.append([rand.randint(min_limit, max_limit), rand.randint(min_limit, max_limit)])
    return points


def visualize_points(points, min_limit, max_limit):
    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], s=15)

    plt.xlim(0)
    plt.ylim(0)
    plt.xticks(np.arange(min_limit, max_limit + 1, step=1))
    plt.yticks(np.arange(min_limit, max_limit + 1, step=1))

    plt.title(f"Set {len(points)} points")

    plt.show()



if __name__ == '__main__':
    points = random_generate_points(30, 1, 15)
    points = np.array(points)
    print(points)
    visualize_points(points, 0, 15)