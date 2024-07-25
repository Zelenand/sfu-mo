from method_fibonacci import fibonacci_method

def norm(vector):
    return (vector[0]**2 + vector[1]**2) ** 0.5

def gauss_zeidel(f, df1, df2, x0, eps1, eps2, M):
    global cache_0
    global cache_1
    global cache_2
    n = len(x0)
    if M % n != 0:
        print("Incorrect M")
        return 0
    df = lambda x: (df1(x), df2(x))
    j = 0
    k = 0
    x = []
    x.append([])
    x[0].append(x0)
    check3 = False
    while True:
        #3
        if j >= M:
            return x[j][k]
        k = 0
        while True:
            #5
            if k == n:
                x.append([])
                x[j+1].append(None)
                x[j + 1][0] = x[j][n]
                j = j + 1
                break
            dfjk = df(x[j][k])
            if norm(dfjk) < eps1:
                return x[j][k]
            if k + 1 == 1:
                dfk = df1
            else:
                dfk = df2
            if k+1 == 1:e = (1, 0)
            else:e = (0, 1)
            tk_func = lambda tk: f((x[j][k][0] - tk * dfk(x[j][k]) * e[0], x[j][k][1] - tk * dfk(x[j][k]) * e[1]))
            tk = fibonacci_method(tk_func)
            x[j].append(None)
            x[j][k+1] = (x[j][k][0] - tk * dfk(x[j][k]) * e[0], x[j][k][1] - tk * dfk(x[j][k]) * e[1])

            check1 = norm((x[j][k+1][0] - x[j][k][0], x[j][k+1][1] - x[j][k][1])) < eps2
            check2 = abs(f(x[j][k+1]) - f(x[j][k])) < eps2
            if check1 and check2:
                if check3:
                    return x[j][k+1]
                check3 = True
            else:
                check3 = False
                k = k + 1