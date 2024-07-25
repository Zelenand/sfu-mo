import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
cache = {}
def func_0(x):
    if x not in cache:
        cache[x] = (x[0] - 1)**2 + (x[1] + x[0])**2
    return cache[x]

func = func_0
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = func((x, y))

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector(x, y)

    def c(self):
        return (self.x, self.y)


def nelder_mead(f, v=None, alpha=1.5, beta=0.25, gamma=2.5, epsilon=0.0001):
    if v is None:
        n = 3
        v1 = Vector(-20, -20)
        v2 = Vector(-20, 20)
        v3 = Vector(20, 20)
        v4 = Vector(20, -20)
        x = [None]
        x.extend([v1, v2, v3, v4])
    else:
        x = [None]
        x.extend(v)
        n = len(v) - 1
    work = True
    x.append(None)
    x.append(None)
    x.append(None)
    x.append(None)
    x.append(None)

    while work:
        x_l = sorted(x[1:n + 2], key=lambda i: i.f)[0]
        x_s = sorted(x[1:n + 2], key=lambda i: i.f)[-2]
        x_h = sorted(x[1:n + 2], key=lambda i: i.f)[-1]
        x[n + 2] = Vector(0, 0)
        for i in sorted(x[1:n + 2], key=lambda i: i.f)[1:n + 1]:
            x[n + 2] += i
        x[n + 2] /= n
        sigma = 0
        for j in range(1, n+2):
            sigma += (x[j].f - x[n+2].f) ** 2
        sigma = (sigma / (n + 1)) ** 0.5
        if sigma <= epsilon:
            return x_l.c(), len(cache)
        else:
            x[n + 3] = x[n + 2] + alpha * (x[n + 2] - x_h)
            if x[n + 3].f <= x_l.f:
                x[n + 4] = x[n + 2] + gamma * (x[n + 3] - x[n + 2])
                if x[n + 4].f < x_l.f:
                    x[x.index(x_h)] = x[n + 4]
                    continue
                else:
                    x[x.index(x_h)] = x[n + 3]
                    continue
            elif x_s.f < x[n + 3].f and x[n + 3].f <= x_h.f:
                x[n + 5] = x[n + 2] + beta * (x_h - x[n + 2])
                x[x.index(x_h)] = x[n + 5]
                continue
            elif x_l.f < x[n + 3].f and x[n + 3].f <= x_s.f:
                x[x.index(x_h)] = x[n + 3]
                continue
            elif x[n + 3].f > x_h.f:
                for j in range(1, n + 2):
                    x[j] = x_l + 0.5 * (x[j] - x_l)
                continue

    return 0

real_x = (1, -1)
alpha=2
beta=0.25
gamma=2.5
epsilon=0.0001
v = [Vector(-20, -20), Vector(-20, 20), Vector(20, 20), Vector(20, -20)]
print("Result of Nelder-Mead algorithm: ")
minimum, calc_num = nelder_mead(func, v, alpha =alpha, beta=beta, gamma=gamma, epsilon=epsilon)
cache = {}
print("Минимум функции:", minimum)
print("Количество вычислений функции:", calc_num)


import matplotlib.pyplot as plt
import numpy as np

def plots(parameters, p):
    global cache
    global real_x
    real_minimum = func(real_x)
    mins = []
    calcs = []
    for i in parameters:
        if p == "v":
            min, calc = nelder_mead(func, i, alpha, beta, gamma, epsilon)
        elif p == "epsilon":
            min, calc = nelder_mead(func, None, alpha, beta, gamma, i)
        elif p == "alpha":
            min, calc = nelder_mead(func, None, i, beta, gamma, epsilon)
        elif p == "beta":
            min, calc = nelder_mead(func, None, alpha, i, gamma, epsilon)
        elif p == "gamma":
            min, calc = nelder_mead(func, None, alpha, beta, i, epsilon)
        cache = {}
        mins.append(abs(func(min) - real_minimum))
        calcs.append(calc)

    if p =="v":
        parameters = [len(i) for i in parameters]
    plt.plot(parameters, mins)
    plt.ylabel("Отклонения от реального минимума")
    plt.xlabel("Параметр " + p)
    plt.show()

    plt.plot(parameters, calcs)
    plt.ylabel("Кол-во вычислений целевой функции")
    plt.xlabel("Параметр " + p)
    plt.show()

v3 = [Vector(0, 1), Vector(1, -1), Vector(-1, -1)]
v4 = [Vector(-20, -20), Vector(-20, 20), Vector(20, 20), Vector(20, -20)]
v5 = [Vector(-20, -20), Vector(-20, 20), Vector(20, 20), Vector(20, -20), Vector(-30, 20)]
v6 = [Vector(-20, -20), Vector(-20, 20), Vector(20, 20), Vector(20, -20), Vector(-40, 20), Vector(-20, 40)]
parameters = [v3, v4, v5, v6]
p = "v"
plots(parameters, p)

parameters = np.arange(0.000001, 0.01, 0.00001)
p = "epsilon"
plots(parameters, p)

parameters = np.arange(2, 3, 0.1)
p = "alpha"
plots(parameters, p)

parameters = np.arange(2, 3, 0.1)
p = "gamma"
plots(parameters, p)

parameters = np.arange(0.1, 0.9, 0.05)
p = "beta"
plots(parameters, p)
