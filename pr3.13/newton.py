#from method_fibonacci import fibonacci_method
import numpy as np
from numpy.linalg import inv, det

cache_0 = {}
cache_1 = {}
cache_2 = {}

def func(x):
    x = tuple(x)
    if x not in cache_0:
        cache_0[x] = (x[0] - 1)**2 + (x[1] + x[0])**2
    return cache_0[x]

def func_d1(x):
    x = tuple(x)
    if x not in cache_1:
        cache_1[x] = 4 * x[0] + 2 * x[1] - 2
    return cache_1[x]

def func_d1_1(x):
    return 4

def func_d2(x):
    x = tuple(x)
    if x not in cache_2:
        cache_2[x] = 2 * x[0] + 2 * x[1]
    return cache_2[x]

def func_d2_2(x):
    return 2

def func_d2_1__1_2(x):
    return 2

def hesse(x):
    h = np.array([[func_d1_1(x), func_d2_1__1_2(x)], [func_d2_1__1_2(x), func_d2_2(x)]])
    h_1 = inv(h)
    return h, h_1


def norm(vector):
    return (vector[0]**2 + vector[1]**2) ** 0.5

def newton(f, df1, df2, x0, eps1, eps2, M):
    global cache_0
    global cache_1
    global cache_2
    df = lambda x: (df1(x), df2(x))
    k = 0
    x = [x0]
    d = [None]
    check3 = False
    while True:
        dfk = df(x[k])
        if norm(dfk) < eps1 or k >= M:
            result = x[k]
            break
        h, h_1 = hesse(x[k])
        if k + 1 > len(d):
            d.append(None)
        if det(h_1) > 0:
            d[k] = - np.matmul(h_1, np.array(dfk))
            tk = 1
            x.append(None)
            x[k + 1] = np.array(x[k]) + tk * d[k]
        else:
            d[k] = - np.array(dfk)
            tk = 1
            x_1 = np.array(x[k]) + tk * d[k]
            if f(x_1) < f(x[k]):
                x.append(None)
                x[k + 1] = x_1
            else:
                tk = -1
                x__1 = np.array(x[k]) + tk * d[k]
                if f(x_1) < f(x[k]):
                    x.append(None)
                    x[k + 1] = x__1
                else:
                    raise Exception("tk error")
        check1 = norm(tuple(x[k+1] - x[k])) < eps2
        check2 = abs(f(tuple(x[k+1])) - f(tuple(x[k]))) < eps2
        if check1 and check2:
            if check3:
                return x[k + 1]
            check3 = True
        else:
            check3 = False
        k = k + 1

    return result

x0 = (10, 10)
real_x = (1, -1)
eps1 = 0.0001
eps2 = 0.0001
M = 300
print("Result of algorithm: ")
minimum = newton(func, func_d1 ,func_d2, x0, eps1, eps2, M)
print("X0:", x0)
print("eps1:", eps1, ", eps2:", eps2, ", M:", M)
print("Минимум функции:", minimum)
print("Количество вычислений функции:", len(cache_0) + len(cache_1) + len(cache_2))
cache_0 = {}
cache_1 = {}
cache_2 = {}

import matplotlib.pyplot as plt
import numpy as np

def plots(parameters, p):
    global cache_0
    global cache_1
    global cache_2
    global real_x
    real_minimum = func(real_x)
    mins = []
    calcs = []
    for i in parameters:
        print(i)
        if p == "X0":
            min = newton(func, func_d1 ,func_d2, i, eps1, eps2, M,)
        elif p == "epsilon1":
            min = newton(func, func_d1 ,func_d2, x0, i, eps2, M)
        elif p == "epsilon2":
            min = newton(func, func_d1 ,func_d2, x0, eps1, i, M)
        elif p == "M":
            min = newton(func, func_d1 ,func_d2, x0, eps1, eps2, i)
        calc = len(cache_0) + len(cache_1) + len(cache_2)
        cache_0 = {}
        cache_1 = {}
        cache_2 = {}
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
    X1 = [10, 10]
    X2 = [100, 100]
    X3 = [1000, 1000]
    parameters = [X0, X1, X2, X3]
    p = "X0"
    plots(parameters, p)

    parameters = np.arange(0.00001, 1, 0.00001)
    p = "epsilon1"
    plots(parameters, p)

    parameters = np.arange(0.00001, 1, 0.00001)
    p = "epsilon2"
    plots(parameters, p)

    parameters = [6, 60, 600]
    p = "M"
    plots(parameters, p)