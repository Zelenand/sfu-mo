"""
Метод Пауэлла (квадратичная интерполяция)
"""
import math
def quad_inter_method(func, x1, delta=0.01, eps1=1e-3, eps2=1e-3):
    work = True
    check = True
    calc_num = 0
    while work:
        if check:
            x2 = x1 + delta
            f1 = func(x1)
            f2 = func(x2)
            calc_num+=2
            if f1 > f2:
                x3 = x1 + 2 * delta
            else:
                x3 = x1 - delta
            f3 = func(x3)
            calc_num += 1
        else:
            f1 = func(x1)
            f2 = func(x2)
            f3 = func(x3)
            calc_num += 3
        F_min = min([f1, f2, f3])
        if F_min == f1: x_min = x1
        elif F_min == f2: x_min = x2
        else: x_min = x3
        numerator = (x2**2 - x3**2) * f1 + (x3**2 - x1**2) * f2 + (x1**2 - x2**2) * f3
        denominator = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3
        if denominator == 0:
            x1 = x_min
            check = True
            continue
        x_poli = 0.5 * (numerator / denominator)
        if x_poli == 0:
            x_poli += eps2 / 2
        f_poli = func(x_poli)
        calc_num += 1
        if (abs((F_min - f_poli) / f_poli) < eps1) and (abs((x_min - x_poli) / x_poli) < eps2):
            work = False
        else:
            interval = sorted([x1, x3])
            if x_poli >= interval[0] and x_poli <= interval[1]:
                if min([F_min, f_poli]) == F_min: x_choosed = x_min
                else:
                    x_choosed = x_poli
                dots = sorted(list(set([x1, x2, x3, x_choosed, x_poli, x_min])))
                x_choosed_i = dots.index(x_choosed)

                if x_choosed_i == 0: x1, x2, x3 = [dots[0], dots[1], dots[2]]
                elif x_choosed_i == len(dots) - 1: x1, x2, x3 = [dots[len(dots) - 3], dots[len(dots) - 2], dots[len(dots) - 1]]
                else:x1, x2, x3 = [dots[x_choosed_i - 1], dots[x_choosed_i], dots[x_choosed_i + 1]]
                check = False
            else:
                x1 = x_poli
                check = True
    return x_poli