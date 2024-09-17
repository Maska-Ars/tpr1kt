import csv
import statistics

from functions import calculate, correlation
# 17-32 болезни
# 0-16 параметры


def read(file: str) -> list[list]:
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        return [line for line in reader]


# Преобразование на отрезок [2:102]
def permutate(l: list[float]) -> list[float]:
    m = max(l)
    return [2 + i / m * 100 for i in l]


# Расчет корреляции Пирсона
def pirson(x: list[float], y: list[float]) -> float:
    return correlation(x, y, method='linear')


def main():
    l = read('Показатели 2005-2018 (24-01-20).csv')
    l[0][0] = 'ГОД'
    print(l[0][19])
    l = [line[2:] for line in l[1:-46]]
    for i in range(0, len(l)):
        for j in range(0, len(l[0])):
            l[i][j] = l[i][j].replace(' ', '')
            if ',' in l[i][j]:
                l[i][j] = l[i][j].replace(',', '.')
            l[i][j] = float(l[i][j])

    n = 16 + 1  # Индекс болезни

    print(l[0][n])
    vec_y = [y[n] for y in l]  # управляемый фактор

    vec_x = [y[0] for y in l]  # управляющий фактор
    print(max(vec_x), min(vec_x))
    print(sum(vec_x)/len(vec_x))

    # Преобразование отрезка на отрезок [2, 102]
    vex_x = permutate(vec_x)

    # Применение функций
    vfx = calculate(vex_x)

    for fx in vfx:
        print(fx)
    print()
    # расчет корреляции пирсона
    vr = []
    for fx in vfx:
        if fx[0] == sum(fx) / len(fx):
            continue
        vr.append(pirson(fx, vec_y))

    for i in range(0, len(vr)):
        if vr[i] < 0:
            vr[i] = -vr[i]
    print(pirson(vec_x, vec_y))
    print(max(vr))


if __name__ == '__main__':
    main()
