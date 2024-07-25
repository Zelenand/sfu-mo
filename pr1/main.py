"""
Метод фибоначчи
Вариант 24
"""
import math

def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_method(func, a, b, l, eps=1e-9):
    n = 1
    while fibonacci(n) < abs(b - a) / l:
        n += 1

    fibonacci_values = []
    for i in range(1, n + 2):
        fibonacci_values.append(fibonacci(i))

    z = a + (fibonacci_values[n - 2] / fibonacci_values[n]) * (b - a)
    z_func = func(z)
    y = a + (fibonacci_values[n - 1] / fibonacci_values[n]) * (b - a)
    y_func = func(y)
    calc_num = 2

    for i in range(1, n + 1):
        if z_func > y_func:
            a = z
            z = y
            z_func = y_func
            y = a + (fibonacci_values[n - i - 1] / fibonacci_values[n - i]) * (b - a)
            if i != n - 2:
                y_func = func(y)
                calc_num += 1
        else:
            b = y
            y = z
            y_func = z_func
            z = a + (fibonacci_values[n - i - 2] / fibonacci_values[n - i]) * (b - a)
            if i != n - 2:
                z_func = func(z)
                calc_num += 1

        if i == n - 2:
            break

    y = z + eps
    y_func = func(y)
    z_func = func(z)
    calc_num = calc_num + 2
    if y_func == z_func:
        a = z
    else:
        b = y
    return (a + b) / 2, calc_num

def func(x):
    return (2 * math.exp(5 * x)) - (6 * x) + (2 * math.pow(x, 3))

def func_2(x):
    return x**2

a, b = -6, 6
l = 0.00001
eps = 1e-9
minimum, calc_num = fibonacci_method(func, a, b, l, eps)
print("Параметры метода: l -", l, ", epsilon -", eps)
print("Минимум функции:", minimum)
print("Количество вычислений функции:", calc_num)

import matplotlib.pyplot as plt
import numpy as np

def plots():
    real_minimum = func(-6)
    parameters = np.arange(0.00001, 1, 0.00001)
    mins = []
    calcs = []
    for i in parameters:
        min, calc = fibonacci_method(func, a, b, i)
        mins.append(abs(func(min) - real_minimum))
        calcs.append(calc)

    plt.plot(parameters, mins)
    plt.ylabel("Отклонения от реального минимума")
    plt.xlabel("Параметр l")
    plt.show()

    plt.plot(parameters, calcs)
    plt.ylabel("Кол-во вычислений целевой функции")
    plt.xlabel("Параметр l")
    plt.show()
