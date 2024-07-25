from method_fibonacci import fibonacci_method

def norm(vector):
    return (vector[0]**2 + vector[1]**2) ** 0.5

def gradient_descent(f, df1, df2, x0, eps1, eps2, M):
    global cache_0
    global cache_1
    global cache_2
    df = lambda x: (df1(x), df2(x))
    k = 0
    x = [x0]
    while True:
        dfk = df(x[k])
        if norm(dfk) < eps1 or k >= M:
            result = x[k]
            break
        tk_func = lambda tk: f((x[k][0] - tk * dfk[0], x[k][1] - tk * dfk[1]))
        tk = fibonacci_method(tk_func)
        x.append(None)
        x[k + 1] = (x[k][0] - tk * dfk[0], x[k][1] - tk * dfk[1])
        check1 = norm((x[k+1][0] - x[k][0], x[k+1][1] - x[k][1])) < eps2
        check2 = abs(f(x[k+1]) - f(x[k])) < eps2
        if check1 and check2:
            result = x[k+1]
            break
        k = k + 1

    return result