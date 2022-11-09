import numpy as np
import matplotlib.pyplot as plt

from inputFunction import function_z

def calculate_eror(sim, name_membership):
    x_y_2d = np.arange(0, 1.01, 0.2)
    z_2d = np.zeros_like(x_y_2d)
    real_function_2d = function_z(x_y_2d, x_y_2d)

    for i in range(len(x_y_2d)):
        sim.input['mx'] = x_y_2d[i]
        sim.input['my'] = x_y_2d[i]
        print(x_y_2d[i], "mx/my")
        sim.compute()
        z_2d[i] = sim.output['mf']
        print(z_2d[i], "mf")

    error = sum(abs((real_function_2d + 1) - (z_2d + 1)) / (real_function_2d + 1)) / len(x_y_2d) * 100

    fig = plt.figure(figsize=(7, 6))
    plt.plot(x_y_2d, z_2d)
    plt.plot(x_y_2d, real_function_2d)
    plt.legend(['modeling function', 'real function'])
    plt.title("Порівняння моделі побудованою за допопомогою " + name_membership + " та оригінальної\n" +
              "E=" + str(error) + "%")
    plt.xlabel("mx == my")
    plt.ylabel("mf")
    plt.show()

