import numpy as np


cache = {}

def func_0(x):
    x = tuple(x)
    if x not in cache:
        cache[x] = (x[0] - 1)**2 + (x[1] + x[0])**2
    return cache[x]

b = -0.5
gamma = 2
e = 0.001
a = 2
N = 10
deltas = [0.01, 0.01]
def rosenbrok(func, x0, e, a=2, b=-0.5, N=10, deltas_0=None):
    if deltas_0 is None:
        deltas_0 = [0.01, 0.01]
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