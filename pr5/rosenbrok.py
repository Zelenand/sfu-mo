import numpy as np

cache = {}

def func_0(x):
    x = tuple(x)
    if x not in cache:
        cache[x] = (x[0] - 1)**2 + (x[1] + x[0])**2
    return cache[x]

def rosenbrok(func, x0, a, b, e, N, deltas_0):
    n = len(x0)
    deltas = {i + 1: deltas_0[i] for i in range(n)}
    d = {}
    for i in range(1, n + 1):
        lst = [0] * n
        lst[i - 1] = 1
        d[i] = np.array(lst)

    x = {0: x0}
    y = {}
    y[1] = x[0]
    k = 0
    i = 1
    l = 0
    end = False

    while not end:
        if func(y[i] + deltas[i] * d[i]) < func(y[i]):
            l = 0
            y[i + 1] = y[i] + deltas[i] * d[i]
            deltas[i] = a * deltas[i]

        else:
            l += 1
            y[i + 1] = y[i]
            deltas[i] = b * deltas[i]
        if i < n:
            i += 1
            continue
        else:
            if func(y[n + 1]) < func(y[1]):
                y[1] = y[n + 1]
                i = 1
                continue
            else:
                if not (func(y[n + 1]) < func(x[k])):
                    if l <= N:
                        if all([abs(t) <= e for t in deltas]):
                            result = x[k]
                            break
                        else:
                            y[1] = y[n + 1]
                            continue
                x[k + 1] = y[n + 1]
                if (
                    (x[k + 1][0] - x[k][0]) ** 2 + (x[k + 1][1] - x[k][1]) ** 2
                ) ** 0.5 <= e:
                    result = x[k + 1]
                    break
                else:
                    lambdas = {}
                    lambdas[1] = x[k + 1][0] - x[k][0]
                    lambdas[2] = x[k + 1][1] - x[k][1]

                    alphas = {}
                    for i in range(1, n + 1):
                        if lambdas[i] == 0:
                            alphas[i] = d[i]
                        else:
                            alphas[i] = sum([lambdas[j] * d[j] for j in range(i, n + 1)])
                    bs = {}
                    d = {}
                    for i in range(1, n + 1):
                        if i == 1:
                            bs[i] = alphas[i]
                        else:
                            bs[i] = alphas[i] - (alphas[1] * d[1])[1] * d[1]
                        d[i] = bs[i] / ((bs[i][0] ** 2 + bs[i][1] ** 2) ** 0.5)

                    i = 1
                    y[1] = x[k + 1]
                    k += 1
                    deltas = {i + 1: deltas_0[i] for i in range(n)}
    return result

func = func_0
real_x = (1, -1)
real = func(real_x)
b = -0.5
gamma = 2
e = 0.001
a = 2
N = 10
deltas = [0.01, 0.01]

x = rosenbrok(func, [0, 0], a, b, e, N, deltas)

print(f"b: {b} - коэффициент сжатия")
print(f"a: {a} - коэффициент растяжения")
print(f"N: {N} - максимальное число неудачных серий шагов по всем направлениям ")
print(f"e: {e} - точность epsilon")
print(f"deltas: {deltas}")
print("Минимум функции:", x)
print("Количество вычислений функции:", len(cache))



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
        if p == "a":
            min = rosenbrok(func, [0, 0], i, b, e, N, deltas)
            calc = len(cache)
        elif p == "b":
            min = rosenbrok(func, [0, 0], a, i, e, N, deltas)
            calc = len(cache)
        elif p == "epsilon":
            min = rosenbrok(func, [0, 0], a, b, i, N, deltas)
            calc = len(cache)
        elif p == "N":
            min = rosenbrok(func, [0, 0], a, b, e, i, deltas)
            calc = len(cache)
        elif p == "deltas":
            min = rosenbrok(func, [0, 0], a, b, e, N, i)
            calc = len(cache)
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


parameters = np.arange(0.000001, 0.1, 0.00001)
p = "epsilon"
plots(parameters, p)

parameters = np.arange(-1, 0, 0.01)
p = "b"
plots(parameters, p)

parameters = np.arange(1, 5, 0.01)
p = "a"
plots(parameters, p)

parameters = np.arange(1, 10, 1)
p = "N"
plots(parameters, p)

parameters = np.arange(0.01, 1, 0.01)
parameters = [[i, i] for i in parameters]
p = "deltas"
plots(parameters, p)