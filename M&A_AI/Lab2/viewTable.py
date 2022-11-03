from inputFunction import function_z


def calculate_tables(mx, my, mf):
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