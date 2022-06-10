import math


def main(y, x, z):
    n = len(y)
    tmp = 0
    for i in range(1, n + 1):
        tmp += 2 * (y[n - math.ceil(i / 4)] + x[n - i] ** 3 + z[n - i] ** 2) ** 3
    return tmp


print(main([-0.39, -0.66, -0.35, 0.2, 0.21, 0.22, -0.08], [0.1, -0.53, 0.61, 0.65, 0.83, -0.51, -0.99],
           [0.6, 0.75, -0.46, -0.59, -0.89, -0.86, -0.97]))
