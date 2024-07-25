from method_fibonacci import fibonacci_method
import numpy as np


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