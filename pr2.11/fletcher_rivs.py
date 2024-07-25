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

cache_0 = {}
def f_01(x):
    x = tuple(x)
    if x not in cache_0:
        cache_0[x] = 2*(x[0]**2) + x[1] * x[0] + x[1]**2
    return cache_0[x]

cache_1 = {}
def d_f_0_11(x):
    x = tuple(x)
    if x not in cache_1:
        cache_1[x] = 4 * x[0] + x[1]
    return cache_1[x]

cache_2 = {}
def d_f_0_21(x):
    x = tuple(x)
    if x not in cache_2:
        cache_2[x] = x[0] + 2 * x[1]
    return cache_2[x]

def norm(vector):
    return (vector[0]**2 + vector[1]**2) ** 0.5

def fletcher_rivs(f, df1, df2, x0, eps1, eps2, M):
    global cache_0
    global cache_1
    global cache_2
    df = lambda x: (df1(x), df2(x))
    check3 = False
    k = 0
    x = [x0]
    d = [None]
    b = [None]
    d_0 = (df(x[0]))
    while True:
        dfk = df(x[k])
        if norm(dfk) < eps1 or k >= M:
            result = x[k]
            break
        if k == 0:
            d[0] = (-d_0[0], -d_0[1])
        else:
            if k-1+1 > len(b):
                b.append(None)
            b[k-1] = (norm(dfk)**2) / (norm(df(x[k-1]))**2)
            if k+1 > len(d):
                d.append(None)
            d[k] = (-dfk[0], -dfk[1]) + (b[k-1] * d[k-1][0], b[k-1] * d[k-1][1])
        tk_func = lambda tk: f((x[k][0] + tk * d[k][0], x[k][1] + tk * d[k][1]))
        cache_0_1 = cache_0.copy()
        cache_1_1 = cache_1.copy()
        cache_2_1 = cache_2.copy()
        tk = fibonacci_method(tk_func)
        cache_0 = cache_0_1.copy()
        cache_1 = cache_1_1.copy()
        cache_2 = cache_2_1.copy()
        x.append(None)
        x[k + 1] = (x[k][0] + tk * d[k][0], x[k][1] + tk * d[k][1])
        check1 = norm((x[k+1][0] - x[k][0], x[k+1][1] - x[k][1])) < eps2
        check2 = abs(f(x[k+1]) - f(x[k])) < eps2
        if check1 and check2:
            if check3:
                return x[k + 1]
            check3 = True
        else:
            check3 = False
        k = k + 1

    return result

x0 = (10, 10)
real_x = (0, 0)
eps1 = 0.0001
eps2 = 0.0001
M = 60
print("Result of algorithm: ")
minimum = fletcher_rivs(f_0, d_f_0_1 ,d_f_0_2, x0, eps1, eps2, M)
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
            min = fletcher_rivs(f_0, d_f_0_1, d_f_0_2, i, eps1, eps2, M,)
        elif p == "epsilon1":
            min = fletcher_rivs(f_0, d_f_0_1, d_f_0_2, x0, i, eps2, M)
        elif p == "epsilon2":
            min = fletcher_rivs(f_0, d_f_0_1, d_f_0_2, x0, eps1, i, M)
        elif p == "M":
            min = fletcher_rivs(f_0, d_f_0_1, d_f_0_2, x0, eps1, eps2, i)
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