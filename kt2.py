from decimal import Decimal, getcontext  # Для работы с числами с заданной точностью
from functions import (
    pairwise_product,
    correlation
)  # Для расчетов

from first_stage import gen_all_models
from second_stage import cor_model
from third_stage import search_vector_k


from data_preprocessing import run, AlgTh  # Для расчетов

from conversion import dict_to_json, json_to_dict, csv_to_dict  # Для сохранения и чтения данных
from symmetry import check_symmetry

from time import time

# 17-32 болезни
# 0-16 параметры

getcontext().prec = 64  # Точность вычислений


def compare_correlation(file1: str = 'data_pairwise_product.json', file2: str = 'func_y1.json'):
    data1 = json_to_dict(file1)

    data2 = json_to_dict(file2)

    y = data2['y'][list(data2['y'].keys())[0]]

    data1_cor = {}
    data2_cor = {}

    for x in data2['functions'].keys():
        if len(data2['functions'][x]) == 2:
            data2_cor.setdefault(x, correlation(data2['x'][x], y))
            data1_cor.setdefault(x, correlation(data1['x'][x], y))

    for x in data1_cor.keys():
            print(x, abs(round(data1_cor[x],4)), abs(round(data2_cor[x], 4)),  data2['functions'][x], round(abs(round(data2_cor[x],4)) / abs(round(data1_cor[x], 4)) ))


def main():
    data = json_to_dict('data.json')
    y = [float(i) for i in data['y']['y3']]
    y = set(data['y']['y3'])
    new_y = [float(i)-float(sum(y)/len(y)) for i in set(data['y']['y3'])]
    print(min(y), max(y), sum(y)/len(y))
    print()

    print(f'w^2 = {check_symmetry(new_y)}')
    all_y = [float(i) for i in data['y']['y3']]

    y2018 = all_y[-1:-1*77-1:-1]
    years = {'2018': y2018[::-1]}

    print(len(y2018), y2018)
    print()

    for i in range(1, 14):
        y_year = all_y[-i*77-1:-(i+1)*77-1:-1]
        years.setdefault(f'{2018-i}', y_year[::-1])

    for i in range(0, 14):
        d = []
        print(f'{2018 - i}')
        for j in range(i+1, 14):
            v = [years[f'{2018 - i}'][k] - years[f'{2018 - j}'][k] for k in range(0, 77)]
            v = list(set(v))
            w = check_symmetry(v)
            print(f'  {2018 - i}-{2018 - j}: w^2 = {w:.5f}, min = {min(v):.5f}, ave = {sum(v)/len(v):.5f}, max = {max(v):.5f}')

            if w > 1.66:
                d.append(f'{2018 - j}')
        print(f'  w^2 > 1.66: {' '.join(d)}')
        print()

    return


if __name__ == '__main__':
    main()
