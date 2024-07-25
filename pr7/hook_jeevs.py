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

    return x[k]