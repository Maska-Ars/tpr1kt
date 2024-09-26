import csv
from decimal import Decimal, getcontext
from functions import calculate, correlation, e1
from data_preprocessing import run, step1
import json

# 17-32 болезни
# 0-16 параметры

getcontext().prec = 64


def read(file: str) -> list[list]:
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        return [line for line in reader]


def list_to_json(l: list) -> None:
    d = {
        'x': {},
        'y': {}
    }
    for i in range(0, 17):
        values = []
        for j in range(1, len(l)):
            values.append(l[j][i])
        d['x'].setdefault(f'x{i+1}', values)
    for i in range(17, 33):
        values = []
        for j in range(1, len(l)):
            values.append(l[j][i])
        d['y'].setdefault(f'y{i-17+1}', values)

    with open('data.json', 'w+') as file:
        json.dump(d, file, indent=2)
    return None


def pairwise_product(data: dict[str, dict[str, list]]) -> None:
    d = {'x': data['x'], 'y': data['y']}
    mx = list(data['x'].keys())
    for i in range(0, len(mx)-1):
        x1 = mx[i]
        x2 = mx[i+1]
        vx1 = data['x'][x1]
        vx2 = data['x'][x2]
        v = []
        for i in range(0, len(vx1)):
            v.append(vx1[i] * vx2[i])
        d['x'].setdefault(f'{x1}*{x2}', v)

    with open('data_pairwise_product.json', 'w+') as file:
        json.dump(d, file, indent=2)
    return None





def main():
    l = read('Показатели 2005-2018 (24-01-20).csv')
    l[0][0] = 'ГОД'
    print(l[0][19])
    l = [line[2:] for line in l[0:-46]]
    for i in range(0, len(l)):
        for j in range(0, len(l[0])):
            l[i][j] = l[i][j].replace(' ', '')
            if ',' in l[i][j]:
                l[i][j] = l[i][j].replace(',', '.')
            try:
                l[i][j] = float(l[i][j])
            except:
                print(l[i][j])

    list_to_json(l)

    with open('data.json', 'r') as file:
        data = json.load(file)

    pairwise_product(data)

    return


    n = 16 + 1  # Индекс болезни
    print(l[0][n])

    vec_y = [y[n] for y in l]  # управляемый фактор
    vec_x = [y[0] for y in l]  # управляющий фактор

    print()
    print()

    matrix = []

    for i in range(0, 16):
        vec_x = [y[i] for y in l]
        x, func = run(vec_x, vec_y)
        matrix.append(x)


if __name__ == '__main__':
    main()
