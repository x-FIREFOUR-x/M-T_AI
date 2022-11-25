import numpy as np
import random as rand
import matplotlib.pyplot as plt
from fcmeans import FCM




def random_generate_points(amount, min_limit, max_limit):
    points = []
    for i in range(0, amount):
        points.append([rand.randint(min_limit, max_limit), rand.randint(min_limit, max_limit)])
    return points


def visualize_points(points, min_limit, max_limit):
    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], marker=".", s=100)

    plt.xlim(0)
    plt.ylim(0)
    plt.xticks(np.arange(min_limit, max_limit + 1, step=1))
    plt.yticks(np.arange(min_limit, max_limit + 1, step=1))

    plt.title(f"Set {len(points)} points")

    plt.show()


def visualize_clusters(points, labels, min_limit, max_limit):
    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], marker=".", s=100, c=labels, cmap='brg')

    plt.xlim(0)
    plt.ylim(0)
    plt.xticks(np.arange(min_limit, max_limit + 1, step=1))
    plt.yticks(np.arange(min_limit, max_limit + 1, step=1))

    plt.title(f"{len(centers)} Clusters points's")

    plt.show()


def visualize_clusters_centers(points, labels, centers, min_limit, max_limit):
    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], marker=".", s=100, c=labels, cmap='brg')
    plt.scatter(centers[:, 0], centers[:, 1], marker="x", s=100, c=range(len(centers)), cmap='brg')

    plt.xlim(0)
    plt.ylim(0)
    plt.xticks(np.arange(min_limit, max_limit + 1, step=1))
    plt.yticks(np.arange(min_limit, max_limit + 1, step=1))

    plt.title(f"{len(centers)} Clusters points's")

    plt.show()


def objective_function(points, max_amount_cluster):
    fpcs = []
    for ncenters in range(2, max_amount_cluster + 1):
        model = FCM(n_clusters=ncenters)
        model.fit(points)
        fpcs.append(model.partition_coefficient)
        p =0

    print("fuzzy partition coefficient for amount clusters (1, ..., 9)")
    print(fpcs)
    plt.plot(np.r_[2:10], fpcs)
    plt.show()



if __name__ == '__main__':
    amount_points = 30
    min_limit = 0
    max_limit = 15
    amount_clusters = 3

    points = np.array(random_generate_points(amount_points, min_limit, max_limit))
    print("Points: ")
    i = 1
    for point in points:
        print(point, end=", ")
        if i % 10 == 0:
            print()
        i += 1
    visualize_points(points, min_limit, max_limit)

    model = FCM(n_clusters=amount_clusters)
    model.fit(points)
    labels = model.predict(points)
    centers = model.centers
    print("\nCenters: ")
    print(centers)
    visualize_clusters(points, labels, min_limit, max_limit)

    visualize_clusters_centers(points, labels, centers, min_limit, max_limit)
    objective_function(points, 9)

