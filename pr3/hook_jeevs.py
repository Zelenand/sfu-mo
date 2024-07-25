import numpy as np


def hook_jeeves(f, x0, eps=0.0000001, d=0.3, h=1, alpha=2):
    n = len(x0)
    delta = d * np.eye(n)

    calc_num = 0
    k = 0
    x = [x0]
    y = [None, x0]

    while True:
        for i in range(1, n + 1):
            fp = f(y[i] + delta[i - 1])
            calc_num+=2
            if fp < f(y[i]):
                if i + 1 >= len(y):
                    y.append(None)
                y[i + 1] = y[i] + delta[i - 1]
            else:
                fm = f(y[i] - delta[i - 1])
                calc_num+=2
                if fm < f(y[i]):
                    if i + 1 >= len(y):
                        y.append(None)
                    y[i + 1] = y[i] - delta[i - 1]
                else:
                    if i + 1 >= len(y):
                        y.append(None)
                    y[i + 1] = y[i]

        calc_num += 2
        if f(y[n+1]) < f(x[k]):
            if k + 1 >= len(x):
                x.append(None)
            x[k + 1] = y[n + 1]
            y[1] = x[k + 1] + h * (x[k + 1] - x[k])
            k = k + 1
        else:
            check = True
            for i in range(0, n):
                if delta[i][i] > eps:
                    delta[i][i] = delta[i][i] / alpha
                    check = False
            if check:
                break
            else:
                y[1] = x[k]
                if k + 1 >= len(x):
                    x.append(None)
                x[k + 1] = x[k]
                k = k + 1

    return x[k], calc_num

def func_0(x):
    # 1 -1
    return (x[0] - 1)**2 + (x[1] + x[0])**2

def func_1(x):
    return x[0]**2 + 6 * (x[1]**2) - 5*(x[1] * x[0]) + 2

def func_2(x):
    return 2  * (x[0]**3) + x[0]**2 - 3 * (x[1]**3) - 2 * x[1] + 2 * (x[1] ** 2)

x0 = [0,0]
eps=0.0000001
d=0.3
h=1
alpha=2
func = func_0
real_x = [1, -1]
minimum, calc_num = hook_jeeves(func, x0, eps, d, h, alpha)
print("Параметры метода: x0 -", x0, ", epsilon -", eps, ", delta -", d, ", lambda -", h, ", alpha -", alpha)
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
        if p == "x0":
            min, calc = hook_jeeves(func, i, eps, d, h, alpha)
        elif p == "epsilon":
            min, calc = hook_jeeves(func, x0, i, d, h, alpha)
        elif p == "delta":
            min, calc = hook_jeeves(func, x0, eps, i, h, alpha)
        elif p == "lambda":
            min, calc = hook_jeeves(func, x0, eps, d, i, alpha)
        elif p == "alpha":
            min, calc = hook_jeeves(func, x0, eps, d, h, i)
        mins.append(abs(func(min) - real_minimum))
        calcs.append(calc)

    plt.plot(parameters, mins)
    plt.ylabel("Отклонения от реального минимума")
    plt.xlabel("Параметр " + p)
    plt.show()

    plt.plot(parameters, calcs)
    plt.ylabel("Кол-во вычислений целевой функции")
    plt.xlabel("Параметр " + p)
    plt.show()

parameters = np.arange(0.000001, 0.01, 0.00001)
p = "epsilon"
plots(parameters, p)

parameters = np.arange(0.01, 0.09, 0.01)
p = "delta"
plots(parameters, p)

parameters = np.arange(0.5, 2, 0.1)
p = "lambda"
plots(parameters, p)

parameters = np.arange(1.1, 2, 0.2)
p = "alpha"
plots(parameters, p)