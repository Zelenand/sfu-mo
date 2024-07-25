import numpy as np
from sympy import symbols, diff, solve
import sympy
from method_fibonacci_for_powell import fibonacci_method

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
            t[i] = fibonacci_method(lambda t: func((args[0] + t, args[1])), eps=fib_eps)
        else:
            t[i] = fibonacci_method(lambda t: func((args[0], args[1] + t)), eps=fib_eps)

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

