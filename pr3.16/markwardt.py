import numpy as np
from numpy.linalg import inv, det


def norm(vector):
    return (vector[0]**2 + vector[1]**2) ** 0.5

def markwardt(f, df1, df2, hesse, x0, eps1, M):
    global cache_0
    global cache_1
    global cache_2
    df = lambda x: (df1(x), df2(x))
    k = 0
    x = [x0]
    d = [None]
    mu = [10000]
    while True:
        check = True
        dfk = df(x[k])
        if norm(dfk) < eps1 or k >= M:
            result = x[k]
            break
        h, _ = hesse(x[k])
        while check:
            if k + 1 > len(d):
                d.append(None)
            d[k] = - np.matmul(inv(h + mu[k] * np.eye(2)), np.array(dfk))
            x.append(None)
            x[k + 1] = np.array(x[k]) + d[k]
            if f(x[k+1]) < f(x[k]):
                mu.append(None)
                mu[k + 1] = mu[k] / 2
                k = k + 1
                check = False
            else:
                mu[k] = 2 * mu[k]

    return result