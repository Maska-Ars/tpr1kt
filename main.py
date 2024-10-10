from decimal import Decimal, getcontext  # Для работы с числами с заданной точностью
from functions import (
    pairwise_product,
    correlation
)  # Для расчетов

from data_preprocessing import run, AlgTh  # Для расчетов

from conversion import dict_to_json, json_to_dict, csv_to_dict  # Для сохранения и чтения данных

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
    ''''# Чтение значений из csv
    data = csv_to_dict('Показатели 2005-2018 (24-01-20).csv')

    # Сохранение значений в json
    dict_to_json(data, 'data.json')

    # Чтение значений из json
    data = json_to_dict('data.json')

    # Добавление попарных произведений
    data = pairwise_product(data)

    # Сохранение значений и попарных произведений
    dict_to_json(data, 'data_pairwise_product.json')

    data = json_to_dict('data_pairwise_product.json')
    # print(data)

    algth = AlgTh(data)
    t = time()
    data = algth.run_all_in_threads(1)
    print((time()-t)/60)

    dict_to_json(data, 'func_y1.json')'''

    compare_correlation()

    return


if __name__ == '__main__':
    main()
