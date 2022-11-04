import numpy as np
import skfuzzy.fuzzymath as fuzzmath
import math
from skfuzzy import control as ctrl

from viewMembershipFunctions import *
from viewTable import *
from inputFunction import view_input_function
from testModel import *


def gauss_membership(mx, my, mf):
    Gxy = 0.085
    Gf = 0.053
    mx["mx1"] = fuzz.gaussmf(mx.universe, Gxy, 0)
    mx["mx2"] = fuzz.gaussmf(mx.universe, Gxy, 0.2)
    mx["mx3"] = fuzz.gaussmf(mx.universe, Gxy, 0.4)
    mx["mx4"] = fuzz.gaussmf(mx.universe, Gxy, 0.6)
    mx["mx5"] = fuzz.gaussmf(mx.universe, Gxy, 0.8)
    mx["mx6"] = fuzz.gaussmf(mx.universe, Gxy, 1)
    mx_max_points = membership_function_gauss(6, Gxy, "mx")

    my["my1"] = fuzz.gaussmf(my.universe, Gxy, 0)
    my["my2"] = fuzz.gaussmf(my.universe, Gxy, 0.4)
    my["my4"] = fuzz.gaussmf(my.universe, Gxy, 0.2)
    my["my3"] = fuzz.gaussmf(my.universe, Gxy, 0.6)
    my["my5"] = fuzz.gaussmf(my.universe, Gxy, 0.8)
    my["my6"] = fuzz.gaussmf(my.universe, Gxy, 1)
    my_max_points = membership_function_gauss(6, Gxy, "my")

    mf["mf1"] = fuzz.gaussmf(mf.universe, Gf, 0)
    mf["mf2"] = fuzz.gaussmf(mf.universe, Gf, 0.125)
    mf["mf3"] = fuzz.gaussmf(mf.universe, Gf, 0.25)
    mf["mf4"] = fuzz.gaussmf(mf.universe, Gf, 0.375)
    mf["mf5"] = fuzz.gaussmf(mf.universe, Gf, 0.5)
    mf["mf6"] = fuzz.gaussmf(mf.universe, Gf, 0.625)
    mf["mf7"] = fuzz.gaussmf(mf.universe, Gf, 0.75)
    mf["mf8"] = fuzz.gaussmf(mf.universe, Gf, 0.875)
    mf["mf9"] = fuzz.gaussmf(mf.universe, Gf, 1)
    mf_max_points = membership_function_gauss(9, Gf, "mf")

    return mx, my, mf, mx_max_points, my_max_points, mf_max_points


def triangle_membership(mx, my, mf):
    mx["mx1"] = fuzz.trimf(mx.universe, [-0.2, 0.0, 0.2])
    mx["mx2"] = fuzz.trimf(mx.universe, [0.0, 0.2, 0.4])
    mx["mx3"] = fuzz.trimf(mx.universe, [0.2, 0.4, 0.6])
    mx["mx4"] = fuzz.trimf(mx.universe, [0.4, 0.6, 0.8])
    mx["mx5"] = fuzz.trimf(mx.universe, [0.6, 0.8, 1.0])
    mx["mx6"] = fuzz.trimf(mx.universe, [0.8, 1.0, 1.2])
    mx_max_points = membership_function_triangle(6, "mx")

    my["my1"] = fuzz.trimf(my.universe, [-0.2, 0.0, 0.2])
    my["my2"] = fuzz.trimf(my.universe, [0.0, 0.2, 0.4])
    my["my3"] = fuzz.trimf(my.universe, [0.2, 0.4, 0.6])
    my["my4"] = fuzz.trimf(my.universe, [0.4, 0.6, 0.8])
    my["my5"] = fuzz.trimf(my.universe, [0.6, 0.8, 1.0])
    my["my6"] = fuzz.trimf(my.universe, [0.8, 1.0, 1.2])
    my_max_points = membership_function_triangle(6, "my")

    mf["mf1"] = fuzz.trimf(mf.universe, [-0.125, 0.00, 0.125])
    mf["mf2"] = fuzz.trimf(mf.universe, [0.000, 0.125, 0.250])
    mf["mf3"] = fuzz.trimf(mf.universe, [0.125, 0.250, 0.375])
    mf["mf4"] = fuzz.trimf(mf.universe, [0.250, 0.375, 0.500])
    mf["mf5"] = fuzz.trimf(mf.universe, [0.375, 0.500, 0.625])
    mf["mf6"] = fuzz.trimf(mf.universe, [0.500, 0.625, 0.750])
    mf["mf7"] = fuzz.trimf(mf.universe, [0.625, 0.750, 0.875])
    mf["mf8"] = fuzz.trimf(mf.universe, [0.750, 0.875, 1.000])
    mf["mf9"] = fuzz.trimf(mf.universe, [0.875, 1.000, 1.250])
    mf_max_points = membership_function_triangle(9, "mf")

    return mx, my, mf, mx_max_points, my_max_points, mf_max_points


def trapation_membership(mx, my, mf):
    mx["mx1"] = fuzz.trapmf(mx.universe, [-0.2, 0.0, 0.1, 0.2])
    mx["mx2"] = fuzz.trapmf(mx.universe, [0.0, 0.2, 0.3, 0.4])
    mx["mx3"] = fuzz.trapmf(mx.universe, [0.2, 0.4, 0.5, 0.6])
    mx["mx4"] = fuzz.trapmf(mx.universe, [0.4, 0.6, 0.7, 0.8])
    mx["mx5"] = fuzz.trapmf(mx.universe, [0.6, 0.8, 0.9, 1.0])
    mx["mx6"] = fuzz.trapmf(mx.universe, [0.8, 1.0, 1.1, 1.2])
    mx_max_points = membership_function_trapation(6, "mx")

    my["my1"] = fuzz.trapmf(my.universe, [-0.2, 0.0, 0.1, 0.2])
    my["my2"] = fuzz.trapmf(my.universe, [0.0, 0.2, 0.3, 0.4])
    my["my3"] = fuzz.trapmf(my.universe, [0.2, 0.4, 0.5, 0.6])
    my["my4"] = fuzz.trapmf(my.universe, [0.4, 0.6, 0.7, 0.8])
    my["my5"] = fuzz.trapmf(my.universe, [0.6, 0.8, 0.9, 1.0])
    my["my6"] = fuzz.trapmf(my.universe, [0.8, 1.0, 1.1, 1.2])
    my_max_points = membership_function_trapation(6, "my")

    mf["mf1"] = fuzz.trapmf(mf.universe, [-0.125, 0.00, 0.0625, 0.125])
    mf["mf2"] = fuzz.trapmf(mf.universe, [0.000, 0.125, 0.1875, 0.250])
    mf["mf3"] = fuzz.trapmf(mf.universe, [0.125, 0.250, 0.3125, 0.375])
    mf["mf4"] = fuzz.trapmf(mf.universe, [0.250, 0.375, 0.4375, 0.500])
    mf["mf5"] = fuzz.trapmf(mf.universe, [0.375, 0.500, 0.5625, 0.625])
    mf["mf6"] = fuzz.trapmf(mf.universe, [0.500, 0.625, 0.6875, 0.750])
    mf["mf7"] = fuzz.trapmf(mf.universe, [0.625, 0.750, 0.8125, 0.875])
    mf["mf8"] = fuzz.trapmf(mf.universe, [0.750, 0.875, 0.9375, 1.000])
    mf["mf9"] = fuzz.trapmf(mf.universe, [0.875, 1.000, 1.0625, 1.250])
    mf_max_points = membership_function_trapation(9, "mf")

    return mx, my, mf, mx_max_points, my_max_points, mf_max_points


def modeling_function_fuzzy_logic(name_function):
    mx = ctrl.Antecedent(np.linspace(0, 1, 6), 'mx')
    my = ctrl.Antecedent(np.linspace(0, 1, 6), 'my')
    mf = ctrl.Consequent(np.linspace(0, 1, 9), 'mf')

    if name_function == "gauss":
        mx, my, mf, mx_max_points, my_max_points, mf_max_points = gauss_membership(mx, my, mf)
    elif name_function == "triangle":
        mx, my, mf, mx_max_points, my_max_points, mf_max_points = triangle_membership(mx, my, mf)
    else:
        mx, my, mf, mx_max_points, my_max_points, mf_max_points = trapation_membership(mx, my, mf)

    calculate_tables(mx_max_points, my_max_points, mf_max_points)
    view_input_function()

    rule_mf1 = ctrl.Rule(antecedent=(mx["mx1"] & my["my1"] |
                                     mx["mx1"] & my["my2"] |
                                     mx["mx1"] & my["my3"] |
                                     mx["mx1"] & my["my4"] |
                                     mx["mx1"] & my["my5"] |
                                     mx["mx1"] & my["my6"]),
                         consequent=mf["mf1"], label="mf1 rule")

    rule_mf2 = ctrl.Rule(antecedent=(mx["mx2"] & my["my3"] |
                                     mx["mx2"] & my["my4"] |
                                     mx["mx2"] & my["my5"] |
                                     mx["mx2"] & my["my6"]),
                         consequent=mf["mf2"], label="mf2 rule")

    rule_mf3 = ctrl.Rule(antecedent=(mx["mx2"] & my["my1"] |
                                     mx["mx2"] & my["my2"] |
                                     mx["mx3"] & my["my5"] |
                                     mx["mx3"] & my["my6"]),
                         consequent=mf["mf3"], label="mf3 rule")

    rule_mf4 = ctrl.Rule(antecedent=(mx["mx3"] & my["my1"] |
                                     mx["mx3"] & my["my2"] |
                                     mx["mx3"] & my["my3"] |
                                     mx["mx3"] & my["my4"] |
                                     mx["mx4"] & my["my5"] |
                                     mx["mx4"] & my["my6"] |
                                     mx["mx5"] & my["my6"]),
                         consequent=mf["mf4"], label="mf4 rule")

    rule_mf5 = ctrl.Rule(antecedent=(mx["mx4"] & my["my3"] |
                                     mx["mx4"] & my["my4"] |
                                     mx["mx5"] & my["my5"] |
                                     mx["mx6"] & my["my6"]),
                         consequent=mf["mf5"], label="mf5 rule")

    rule_mf6 = ctrl.Rule(antecedent=(mx["mx4"] & my["my1"] |
                                     mx["mx4"] & my["my2"] |
                                     mx["mx5"] & my["my4"]),
                         consequent=mf["mf6"], label="mf6 rule")

    rule_mf7 = ctrl.Rule(antecedent=(mx["mx5"] & my["my1"] |
                                     mx["mx5"] & my["my2"] |
                                     mx["mx5"] & my["my3"] |
                                     mx["mx6"] & my["my5"]),
                         consequent=mf["mf7"], label="mf7 rule")

    rule_mf8 = ctrl.Rule(antecedent=(mx["mx6"] & my["my3"] |
                                     mx["mx6"] & my["my4"]),
                         consequent=mf["mf8"], label="mf8 rule")

    rule_mf9 = ctrl.Rule(antecedent=(mx["mx6"] & my["my1"] |
                                     mx["mx6"] & my["my2"]),
                         consequent=mf["mf9"], label="mf9 rule")

    input_ctrl = ctrl.ControlSystem(rules=[rule_mf1, rule_mf2, rule_mf3, rule_mf4, rule_mf5,
                                           rule_mf6, rule_mf7, rule_mf8, rule_mf9])
    sim = ctrl.ControlSystemSimulation(input_ctrl, flush_after_run=36 * 36 + 1)

    upsampled = [0, 0.2, 0.4, 0.6, 0.8, 1]
    x, y = np.meshgrid(upsampled, upsampled)
    z = np.zeros_like(x)

    z_diagonal = np.zeros_like(upsampled)

    for i in range(len(upsampled)):
        for j in range(len(upsampled)):
            sim.input['mx'] = x[i, j]
            sim.input['my'] = y[i, j]
            sim.compute()
            z[i, j] = sim.output['mf']

    fig = plt.figure(figsize=(7, 6))
    fig.suptitle("model " + name_function)
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                           linewidth=0.4, antialiased=True)

    cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
    cset = ax.contourf(x, y, z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
    cset = ax.contourf(x, y, z, zdir='y', offset=3, cmap='viridis', alpha=0.5)

    ax.view_init(30, 200)
    plt.show()

    calculate_eror(sim, name_function)



if __name__ == '__main__':
    is_run = True
    while is_run:
        chosen_func = input("\n *input membership (1-gauss, 2-triangle, 3-trapation, other-exit): ")
        if chosen_func == "1":
            modeling_function_fuzzy_logic("gauss")
        elif chosen_func == "2":
            modeling_function_fuzzy_logic("triangle")
        elif chosen_func == "3":
            modeling_function_fuzzy_logic("trapation")
        else:
            is_run = False





