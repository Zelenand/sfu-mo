from method_fibonacci import fibonacci_method
import numpy as np

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

def func_2(x):
    x = tuple(x)
    if x not in cache_0:
        cache_0[x] = (x[0] - 1)**2 + (x[1] + x[0])**2
    return cache_0[x]

def func_2_d1(x):
    x = tuple(x)
    if x not in cache_1:
        cache_1[x] = 4 * x[0] + 2 * x[1] - 2
    return cache_1[x]

def func_2_d2(x):
    x = tuple(x)
    if x not in cache_2:
        cache_2[x] = 2 * x[0] + 2 * x[1]
    return cache_2[x]

def norm(vector):
    return (vector[0]**2 + vector[1]**2) ** 0.5

def davidon_fletcher_powell(f, df1, df2, x0, eps1, eps2, M):
    global cache_0
    global cache_1
    global cache_2
    df = lambda x: (df1(x), df2(x))
    k = 0
    x = [x0]
    d = [None]
    check3 = False
    A = [np.eye(2)]
    Ac = [None]
    dg = [None]
    dx = [None]
    while True:
        dfk = df(x[k])
        if norm(dfk) < eps1 or k >= M:
            result = x[k]
            break
        if k != 0:
            if k - 1 + 1 > len(dg):
                dg.append(None)
            dg[k-1] = (dfk[0] - df(x[k-1])[0], dfk[1] - df(x[k-1])[1])
            if k - 1 + 1 > len(dx):
                dx.append(None)
            dx[k-1] = (x[k][0] - x[k - 1][0], x[k][1] - x[k - 1][1])
            if k - 1 + 1 > len(Ac):
                Ac.append(None)
            first = np.matmul(np.array(dx[k-1]), np.transpose(dx[k-1])) / np.matmul(np.transpose(dx[k-1]), np.array(dg[k-1]))
            second = (np.matmul(np.matmul(A[k-1], np.array(dg[k-1])), np.transpose(dg[k-1]))*A[k-1]) / (np.matmul(np.matmul(np.transpose(dg[k-1]), A[k-1]), np.array(dg[k-1])))
            Ac[k - 1] = first - second
            if k + 1 > len(A):
                A.append(None)
            A[k] = A[k-1] + Ac[k-1]
        if k + 1 > len(d):
            d.append(None)
        d[k] = - np.matmul(A[k], np.array(dfk))
        tk_func = lambda tk: f(tuple(np.array(x[k]) - tk * np.matmul(d[k], np.array(dfk))))

        tk = fibonacci_method(tk_func)

        x.append(None)
        x[k + 1] = np.array(x[k]) - tk * np.matmul(d[k], np.array(dfk))
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
real_x = (0, 0)
eps1 = 0.0001
eps2 = 0.0001
M = 300
print("Result of algorithm: ")
minimum = davidon_fletcher_powell(f_0, d_f_0_1 ,d_f_0_2, x0, eps1, eps2, M)
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
            min = davidon_fletcher_powell(f_0, d_f_0_1, d_f_0_2, i, eps1, eps2, M,)
        elif p == "epsilon1":
            min = davidon_fletcher_powell(f_0, d_f_0_1, d_f_0_2, x0, i, eps2, M)
        elif p == "epsilon2":
            min = davidon_fletcher_powell(f_0, d_f_0_1, d_f_0_2, x0, eps1, i, M)
        elif p == "M":
            min = davidon_fletcher_powell(f_0, d_f_0_1, d_f_0_2, x0, eps1, eps2, i)
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