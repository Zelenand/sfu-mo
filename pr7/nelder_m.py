import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
class Vector(object):
    def __init__(self, x, y, func):
        self.x = x
        self.y = y
        self.func = func
        self.f = func((x, y))

    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y, self.func)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y, self.func)

    def __rmul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y, self.func)

    def __truediv__(self, other):
        x = self.x / other
        y = self.y / other
        return Vector(x, y, self.func)

    def c(self):
        return (self.x, self.y)


def nelder_mead(f, v=None, alpha=1.5, beta=0.25, gamma=2.5, epsilon=0.0001):
    if v is None:
        n = 3
        v1 = Vector(-20, -20, f)
        v2 = Vector(-20, 20, f)
        v3 = Vector(20, 20, f)
        v4 = Vector(20, -20, f)
        x = [None]
        x.extend([v1, v2, v3, v4])
    else:
        x = [None]
        x.extend(v)
        n = len(v) - 1
    work = True
    x.append(None)
    x.append(None)
    x.append(None)
    x.append(None)
    x.append(None)

    while work:
        x_l = sorted(x[1:n + 2], key=lambda i: i.f)[0]
        x_s = sorted(x[1:n + 2], key=lambda i: i.f)[-2]
        x_h = sorted(x[1:n + 2], key=lambda i: i.f)[-1]
        x[n + 2] = Vector(0, 0, f)
        for i in sorted(x[1:n + 2], key=lambda i: i.f)[1:n + 1]:
            x[n + 2] += i
        x[n + 2] /= n
        sigma = 0
        for j in range(1, n+2):
            sigma += (x[j].f - x[n+2].f) ** 2
        sigma = (sigma / (n + 1)) ** 0.5
        if sigma <= epsilon:
            return x_l.c()
        else:
            x[n + 3] = x[n + 2] + alpha * (x[n + 2] - x_h)
            if x[n + 3].f <= x_l.f:
                x[n + 4] = x[n + 2] + gamma * (x[n + 3] - x[n + 2])
                if x[n + 4].f < x_l.f:
                    x[x.index(x_h)] = x[n + 4]
                    continue
                else:
                    x[x.index(x_h)] = x[n + 3]
                    continue
            elif x_s.f < x[n + 3].f and x[n + 3].f <= x_h.f:
                x[n + 5] = x[n + 2] + beta * (x_h - x[n + 2])
                x[x.index(x_h)] = x[n + 5]
                continue
            elif x_l.f < x[n + 3].f and x[n + 3].f <= x_s.f:
                x[x.index(x_h)] = x[n + 3]
                continue
            elif x[n + 3].f > x_h.f:
                for j in range(1, n + 2):
                    x[j] = x_l + 0.5 * (x[j] - x_l)
                continue
