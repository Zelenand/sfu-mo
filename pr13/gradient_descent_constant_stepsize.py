def norm(dfs):
    return (dfs[0]**2 + dfs[1]**2) ** 0.5

def gradient_descent_constant_stepsize(f, df1, df2, x0, eps1, eps2, M, t = 0.1, eps = None):
    df = lambda x: (df1(x), df2(x))
    k = 0
    x = [x0]
    while True:
        dfk = df(x[k])
        if norm(dfk) < eps1 or k >= M:
            result = x[k]
            break
        tk = t
        x.append(None)
        while True:
            x[k+1] = (x[k][0] - tk * dfk[0], x[k][1] - tk * dfk[1])
            if eps:
                if f(x[k+1]) - f(x[k]) < - eps * (norm(dfk)**2):
                    break
            elif f(x[k+1]) - f(x[k]) < 0:
                break
            tk = tk / 2
        check1 = norm((x[k+1][0] - x[k][0], x[k+1][1] - x[k][1])) < eps2
        check2 = abs(f(x[k+1]) - f(x[k])) < eps2
        if check1 and check2:
            result = x[k+1]
            break
        k = k + 1

    return result