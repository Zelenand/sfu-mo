import numpy as np
from sympy import symbols, diff, solve
import sympy
from method_fibonacci_for_powell import fibonacci_method

cache = {}
def func_0(x):
    x = tuple(x)
    if x not in cache:
        cache[x] = (x[0] - 1)**2 + (x[1] + x[0])**2
    return cache[x]

def func_1(x):
    x = tuple(x)
    if x not in cache:
        cache[x] = 2  * (x[0]**3) + x[0]**2 - 3 * (x[1]**3) - 2 * x[1] + 2 * (x[1] ** 2)
    return cache[x]


def powell(func, x0, e, fib_eps=0.0001):
    n = len(x0)
    d_base = {}
    for i in range(1, n + 1):
        lst = [0] * n
        lst[i - 1] = 1
        d_base[i] = np.array(lst)
    d = {}
    y = {}
    t = {}
    d_base[0] = d_base[n]
    i = 0
    k = 0
    x = {0: x0}
    y[0] = x[0]

    while True:
        args = y[i]
        if d_base[i][0]:
            f = lambda a: func((args[0] + a, args[1]))
        else:
            f = lambda a: func((args[0], args[1] + a))
        t[i] = fibonacci_method(f, eps=fib_eps)

        y[i + 1] = y[i] + t[i] * d_base[i]

        if i < (n - 1):
            i += 1
            continue
        elif i == (n - 1):
            if (y[n][0] == y[0][0]) and (y[n][1] == y[0][1]):
                return y[n]
            i += 1
            continue
        else:
            if (y[n + 1][0] == y[0][0]) and (y[n + 1][1] == y[0][1]):
                return y[n + 1]

        x[k + 1] = y[n + 1]
        if ((x[k + 1][1] - x[k][1]) ** 2 + (x[k + 1][0] - x[k][0]) ** 2) ** 0.5 < e:
            return x[k + 1]
        else:
            d[n] = y[n + 1] - y[1]
            d[0] = d[n]
            d[1] = d_base[2]
            if np.linalg.matrix_rank(np.array([d[0], d[1]])) == n:
                for i in range(n + 1):
                    d[i] = d_base[i]
                i = 0
                y[0] = x[k + 1]
                k = k + 1
                continue
            else:
                for i in range(n + 1):
                    d_base[i] = d[i]
                y[0] = x[k + 1]
                k += 1
                i = 0
                continue


e = 0.01
func = func_0
real_x = [1, -1]
X0 = [0, 0]
print("Result of algorithm: ")
minimum = powell(func, X0, e)
print("X0:", [0, 0])
print("e:", 0.01)
print("Минимум функции:", minimum)
print("Количество вычислений функции:", len(cache))
cache = {}

import matplotlib.pyplot as plt
import numpy as np

def plots(parameters, p):
    global cache
    global real_x
    real_minimum = func(real_x)
    mins = []
    calcs = []
    for i in parameters:
        print(i)
        if p == "X0":
            min = powell(func, i, e)
            calc = len(cache)
        elif p == "epsilon":
            min = powell(func, X0, i)
            calc = len(cache)
        cache = {}
        mins.append(abs(func(min) - real_minimum))
        calcs.append(calc)

    if p =="X0":
        parameters = [i for i in range(len(parameters))]
    plt.plot(parameters, mins)
    plt.ylabel("Отклонения от реального минимума")
    plt.xlabel("Параметр " + p)
    plt.show()

    plt.plot(parameters, calcs)
    plt.ylabel("Кол-во вычислений целевой функции")
    plt.xlabel("Параметр " + p)
    plt.show()

if False:
    X0 = [0, 0]
    X1 = [-2, -2]
    X2 = [-20, -20]
    X3 = [-200, -200]
    parameters = [X0, X1, X2, X3]
    p = "X0"
    plots(parameters, p)

    parameters = np.arange(0.001, 1, 0.001)
    p = "epsilon"
    plots(parameters, p)


