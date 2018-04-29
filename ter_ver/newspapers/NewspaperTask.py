from scipy.optimize import linprog


class NewspaperTask:
    separator = "------------------------------------------------------------------\n"

    def __init__(self, mass_i, dispers, a, b):
        self.mass_i = mass_i
        self.dispers = dispers
        self.a = a
        self.b = b
        self.mat_og = (mass_i[0] + mass_i[-1]) / 2

    def get_line_prog(self, k):
        # if k < self.mass_i[0]:
        #     return self.a * k
        #
        # if k > self.mass_i[-1]:
        #     return self.mat_og * (self.a + self.b) - self.b * k

        min_func = get_min_func(self.mass_i, self.a, self.b, k)
        a = get_a(self.mass_i)
        b = get_b(self.mat_og, self.dispers)

        line_prog = linprog(
            c=min_func,  # minimize function
            A_ub=None, b_ub=None,  # Ax <= b
            A_eq=a, b_eq=b,  # Ax = b
            bounds=(0, None)  # x_i >= 0
        )

        rez_printer = self.separator
        rez_printer += "k = " + str(k) + "\n"
        rez_printer += get_constraint_string(min_func) + " -> min = " + str(line_prog.fun) + "\n"
        rez_printer += "w_i = " + str(print_w(line_prog.x)) + "\n"
        rez_printer += self.separator
        print(rez_printer)

        return line_prog

    def __str__(self):
        rez = self.separator
        rez += "NewspaperTask" + "\n"
        rez += "[alpha, beta] = [" + ', '.join(str(x) for x in self.mass_i) + "]\n"
        rez += "a = " + str(self.a) + "; b = " + str(self.b) + "\n"
        rez += "dispersion = " + str(self.dispers) + "\n"

        rez += "Constraints:\n"
        b_array = get_b(self.mat_og, self.dispers)
        rez += get_constraint_string(get_first_constraint_koef(self.mass_i)) + " = " + str(b_array[0]) + "\n"
        rez += get_constraint_string(get_second_constraint_koef(self.mass_i)) + " = " + str(b_array[1]) + "\n"
        rez += get_constraint_string(get_third_constraint_koef(self.mass_i)) + " = " + str(b_array[2]) + "\n"

        return rez + self.separator


def print_w(x):
    rez = "["
    for i in range(0, len(x)):
        rez += "w" + str(i + 1) + "=" + str(x[i]) + "; "
    return rez[:-2] + "]"


def get_constraint_string(constraint_array):
    rez = ""
    for i in range(0, len(constraint_array)):
        rez += str(constraint_array[i]) + "*w" + str(i + 1) + " + "
    return rez[:-3]


def get_b(mat_og, dispers):
    return [mat_og, dispers + mat_og ** 2, 1]


def get_a(mass_i):
    rez = [get_first_constraint_koef(mass_i),
           get_second_constraint_koef(mass_i),
           get_third_constraint_koef(mass_i)]
    return rez


def get_first_constraint_koef(mass_i):
    return mass_i


def get_second_constraint_koef(mass_i):
    rez = []
    for i in mass_i:
        rez.append(i ** 2)
    return rez


def get_third_constraint_koef(mass_i):
    rez = []
    for _ in mass_i:
        rez.append(1)
    return rez


def get_min_func(mass_i, a, b, k):
    rez = []
    for i in mass_i:
        if i <= k:
            rez.append(a * i - b * (k - i))
        else:
            rez.append(a * k)
    return rez
