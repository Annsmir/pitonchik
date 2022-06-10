def main(b, a, m):
    res = 0
    for c in range(1, m + 1):
        for i in range(1, a + 1):
            for k in range(1, b + 1):
                res += 44 - 37 * pow(3 + 71 * k ** 2 + i, 5) - 13 * pow(c ** 3 - i ** 2, 4)
    return res


print(main(3, 8, 3))
