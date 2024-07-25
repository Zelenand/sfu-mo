from method_fibonacci import fibonacci_method

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
        tk = fibonacci_method(tk_func)
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