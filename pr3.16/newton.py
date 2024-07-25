#from method_fibonacci import fibonacci_method
import numpy as np
from numpy.linalg import inv, det

def norm(vector):
    return (vector[0]**2 + vector[1]**2) ** 0.5

def newton(f, df1, df2, hesse, x0, eps1, eps2, M):
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