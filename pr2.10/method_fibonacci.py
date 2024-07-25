import math

def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

def swann_algorithm(x0, t, func):
    xs = {0:x0}
    k = 0
    y1, y2, y3 = func(xs[0]-t), func(xs[0]), func(xs[0]+t)
    if y1 >= y2 and y2 <= y3:
        return [xs[0]-t,xs[0]+t]
    elif y1 <= y2 and y2 >= y3:
        return -1
    if y1  >= y2 >= y3:
        delta = t
        a = xs[0]
        xs[1] = xs[0] + t
        k = 1
    elif y1  <= y2 <= y3:
        delta = -t
        b = xs[0]
        xs[1] = xs[0] - t
        k = 1
    flag = True
    while flag:
        xs[k+1] =  xs[k] + (2**k)*delta
        if func(xs[k+1]) < func(xs[k]):
            if delta == t:
                a = xs[k]
            if delta == -t:
                b = xs[k]
            k = k+1
        else:
            flag = False
            if delta == t:
                b = xs[k+1]
            if delta == -t:
                a = xs[k+1]
    return a, b

def fibonacci_method(func, l=0.001, eps=1e-9):
    n = 1
    a, b = swann_algorithm(0, 1, func)
    while fibonacci(n) < abs(b - a) / l:
        n += 1

    fibonacci_values = []
    for i in range(1, n + 2):
        fibonacci_values.append(fibonacci(i))

    z = a + (fibonacci_values[n - 2] / fibonacci_values[n]) * (b - a)
    z_func = func(z)
    y = a + (fibonacci_values[n - 1] / fibonacci_values[n]) * (b - a)
    y_func = func(y)

    for i in range(1, n + 1):
        if z_func > y_func:
            a = z
            z = y
            z_func = y_func
            y = a + (fibonacci_values[n - i - 1] / fibonacci_values[n - i]) * (b - a)
            if i != n - 2:
                y_func = func(y)
        else:
            b = y
            y = z
            y_func = z_func
            z = a + (fibonacci_values[n - i - 2] / fibonacci_values[n - i]) * (b - a)
            if i != n - 2:
                z_func = func(z)

        if i == n - 2:
            break

    y = z + eps
    y_func = func(y)
    z_func = func(z)
    if y_func == z_func:
        a = z
    else:
        b = y
    return (a + b) / 2