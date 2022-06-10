def main(y):
    if y < 116:
        return 92 * (y - (y * y * y / 18) - 69)
    elif 116 <= y < 152:
        return pow(40 * y + 43 * y * y, 7)
    elif y >= 152:
        return pow(75 + y * y * y, 6) - (pow(y, 7) / 30)


print(main(155))
