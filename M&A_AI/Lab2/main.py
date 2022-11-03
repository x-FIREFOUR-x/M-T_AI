import skfuzzy.fuzzymath as fuzzmath
import math
from skfuzzy import control as ctrl

from viewFunction import *


def function_z(x, y):
    return x * np.cos(abs(y))

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


def modeling_function_fuzzy_logic(MX, MY, MF):
    Gxy = 0.085
    Gf = 0.053
    mx = ctrl.Antecedent(np.arange(0, 1.2, 0.2), 'mx')
    my = ctrl.Antecedent(np.arange(0, 1.2, 0.2), 'my')
    mf = ctrl.Consequent(np.arange(0, 1.125, 0.125), 'mf')

    mx["mx1"] = fuzz.gaussmf(mx.universe, Gxy, 0)
    mx["mx2"] = fuzz.gaussmf(mx.universe, Gxy, 0.2)
    mx["mx3"] = fuzz.gaussmf(mx.universe, Gxy, 0.4)
    mx["mx4"] = fuzz.gaussmf(mx.universe, Gxy, 0.6)
    mx["mx5"] = fuzz.gaussmf(mx.universe, Gxy, 0.8)
    mx["mx6"] = fuzz.gaussmf(mx.universe, Gxy, 1)

    my["my1"] = fuzz.gaussmf(my.universe, Gxy, 0)
    my["my2"] = fuzz.gaussmf(my.universe, Gxy, 0.4)
    my["my4"] = fuzz.gaussmf(my.universe, Gxy, 0.2)
    my["my3"] = fuzz.gaussmf(my.universe, Gxy, 0.6)
    my["my5"] = fuzz.gaussmf(my.universe, Gxy, 0.8)
    my["my6"] = fuzz.gaussmf(my.universe, Gxy, 1)

    mf["mf1"] = fuzz.gaussmf(mf.universe, Gf, 0)
    mf["mf2"] = fuzz.gaussmf(mf.universe, Gf, 0.125)
    mf["mf3"] = fuzz.gaussmf(mf.universe, Gf, 0.25)
    mf["mf4"] = fuzz.gaussmf(mf.universe, Gf, 0.375)
    mf["mf5"] = fuzz.gaussmf(mf.universe, Gf, 0.5)
    mf["mf6"] = fuzz.gaussmf(mf.universe, Gf, 0.625)
    mf["mf7"] = fuzz.gaussmf(mf.universe, Gf, 0.75)
    mf["mf8"] = fuzz.gaussmf(mf.universe, Gf, 0.875)
    mf["mf9"] = fuzz.gaussmf(mf.universe, Gf, 1)

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
    sim = ctrl.ControlSystemSimulation(input_ctrl)

    upsampled = [0, 0.2, 0.4, 0.6, 0.8, 1]
    x, y = np.meshgrid(upsampled, upsampled)
    z = np.zeros_like(x)

    # Loop through the system 21*21 times to collect the control surface
    for i in range(len(upsampled)):
        for j in range(len(upsampled)):
            sim.input['mx'] = x[i, j]
            sim.input['my'] = y[i, j]
            sim.compute()
            z[i, j] = sim.output['mf']

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                           linewidth=0.4, antialiased=True)

    cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
    cset = ax.contourf(x, y, z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
    cset = ax.contourf(x, y, z, zdir='y', offset=3, cmap='viridis', alpha=0.5)

    ax.view_init(30, 200)
    plt.show()



if __name__ == '__main__':
    mx = membership_function_gauss(6, 0.0850, "mx")
    my = membership_function_gauss(6, 0.0850, "my")
    mf = membership_function_gauss(9, 0.053, "mf")

    x = mx[1]
    tables(mx, my, mf)
    modeling_function()

    modeling_function_fuzzy_logic(mx, my, mf)





