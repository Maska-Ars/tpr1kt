from decimal import getcontext  # Для работы с числами с заданной точностью

from conversion import json_to_dict
import math

# 17-32 болезни
# 0-16 параметры

getcontext().prec = 64  # Точность вычислений


def main():
    data = json_to_dict('data.json')
    y = [float(i) for i in data['y']['y3']]

    k = 1.05

    print(min(y), sum(y) / len(y), max(y))
    print()
    b = True
    while b:
        mi = min(y)
        ave = sum(y) / len(y)
        ma = max(y)

        l = min(abs(mi - ave), abs(ma - ave))

        l = l * k
        remove_value = None
        if abs(mi-ave) > l:
            b = True
            y.remove(mi)
            remove_value = mi
        elif abs(ma-ave) > l:
            b = True
            y.remove(ma)
            remove_value = ma
        else:
            b = False

        print(f'min = {mi}, ave = {ave:.3f}, max = {ma}, l = {l:.3f}, remove_value = {remove_value}')

    print()
    print(len(y))

    print('Эмпирическая область определения')

    emi = min(y) - (max(y)-min(y)) * k
    ema = max(y) + (max(y)-min(y)) * k
    # if emi < 0:
    #     emi = 0
    print(f'min = {emi}')
    print(f'max = {ema}')

    print()
    print('Теоритическая область определения')

    ave = sum(y) / len(y)
    deviation = math.sqrt(sum([(i - ave)**2 for i in y]) / len(y))

    tmi = ave - 3 * deviation
    tma = ave + 3 * deviation

    # if tmi < 0:
    #     tmi = 0

    print(f'min = {tmi}')
    print(f'max = {tma}')
    print()

    print('Симбиоз')

    mi = min(emi, tmi)
    ma = max(ema, tma)

    print(f'min = {mi}')
    print(f'ave = {ave}, {(mi + ma) / 2}')
    print(f'max = {ma}')
    print()

    print('Расширенная область определения')

    k = 1.05
    d = abs(mi - ma) * k - abs(mi - ma)
    print(f'd = {d}, при k = {k}')
    lmi = abs(ave - mi)
    lma = abs(ave - ma)

    if d <= abs(lmi - lma):
        if lmi < lma:
            mi -= d
        else:
            ma += d
    else:
        c = abs(lmi - lma)
        d -= c
        if lmi < lma:
            mi -= c
        else:
            ma += c

        mi -= d / 2
        ma += d / 2

    print()
    print(f'min = {mi}')
    print(f'ave = {ave}, {(mi + ma) / 2}')
    print(f'max = {ma}')

    return


if __name__ == '__main__':
    main()
