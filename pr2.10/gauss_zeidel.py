from method_fibonacci import fibonacci_method


cache_0 = {}
def f_0(x):
    x = tuple(x)
    if x not in cache_0:
        cache_0[x] = x[0]**2 + x[1] * x[0] + 7 * x[1]**2
    return cache_0[x]

cache_1 = {}
def d_f_0_1(x):
    x = tuple(x)
    if x not in cache_1:
        cache_1[x] = 2 * x[0] + x[1]
    return cache_1[x]

cache_2 = {}
def d_f_0_2(x):
    x = tuple(x)
    if x not in cache_2:
        cache_2[x] = x[0] + 14 * x[1]
    return cache_2[x]

def norm(vector):
    return (vector[0]**2 + vector[1]**2) ** 0.5

def gauss_zeidel(f, df1, df2, x0, eps1, eps2, M):
    global cache_0
    global cache_1
    global cache_2
    n = len(x0)
    if M % n != 0:
        print("Incorrect M")
        return 0
    df = lambda x: (df1(x), df2(x))
    j = 0
    k = 0
    x = []
    x.append([])
    x[0].append(x0)
    check3 = False
    while True:
        #3
        if j >= M:
            return x[j][k]
        k = 0
        while True:
            #5
            if k == n:
                x.append([])
                x[j+1].append(None)
                x[j + 1][0] = x[j][n]
                j = j + 1
                break
            dfjk = df(x[j][k])
            if norm(dfjk) < eps1:
                return x[j][k]
            if k + 1 == 1:
                dfk = df1
            else:
                dfk = df2
            if k+1 == 1:e = (1, 0)
            else:e = (0, 1)
            tk_func = lambda tk: f((x[j][k][0] - tk * dfk(x[j][k]) * e[0], x[j][k][1] - tk * dfk(x[j][k]) * e[1]))
            cache_0_1 = cache_0.copy()
            cache_1_1 = cache_1.copy()
            cache_2_1 = cache_2.copy()
            tk = fibonacci_method(tk_func)
            cache_0 = cache_0_1.copy()
            cache_1 = cache_1_1.copy()
            cache_2 = cache_2_1.copy()
            x[j].append(None)
            x[j][k+1] = (x[j][k][0] - tk * dfk(x[j][k]) * e[0], x[j][k][1] - tk * dfk(x[j][k]) * e[1])

            check1 = norm((x[j][k+1][0] - x[j][k][0], x[j][k+1][1] - x[j][k][1])) < eps2
            check2 = abs(f(x[j][k+1]) - f(x[j][k])) < eps2
            if check1 and check2:
                if check3:
                    return x[j][k+1]
                check3 = True
            else:
                check3 = False
                k = k + 1

x0 = (10, 10)
real_x = (0, 0)
eps1 = 0.0001
eps2 = 0.0001
M = 60
print("Result of algorithm: ")
minimum = gauss_zeidel(f_0, d_f_0_1, d_f_0_2, x0, eps1, eps2, M)
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
    real_minimum = f_0(real_x)
    mins = []
    calcs = []
    for i in parameters:
        print(i)
        if p == "X0":
            min = gauss_zeidel(f_0, d_f_0_1, d_f_0_2, i, eps1, eps2, M)
        elif p == "epsilon1":
            min = gauss_zeidel(f_0, d_f_0_1, d_f_0_2, x0, i, eps2, M)
        elif p == "epsilon2":
            min = gauss_zeidel(f_0, d_f_0_1, d_f_0_2, x0, eps1, i, M)
        elif p == "M":
            min = gauss_zeidel(f_0, d_f_0_1, d_f_0_2, x0, eps1, eps2, i)
        calc = len(cache_0) + len(cache_1) + len(cache_2)
        cache_0 = {}
        cache_1 = {}
        cache_2 = {}
        mins.append(abs(f_0(min) - real_minimum))
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