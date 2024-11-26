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

    l = gen_all_models(0.7, 1)[0]
    print()
    model = cor_model(l, 0.13)
    print(len(model), model)

    data = json_to_dict('func_y3.json')
    y = [float(i) for i in data['y']['y3']]
    # print(y)


    mx = [[1 for i in range(0, len(y))]]
    for x in model:
        float_vx = [float(i) for i in data['x'][x]]
        mx.append(float_vx)

    k = search_vector_k(mx, y)
    print(len(k), k)
    m = []
    for i in range(0, len(model)):
        x = model[i]
        kx = k[i+1]
        vx = [float(j)*kx for j in data['x'][x]]
        m.append(vx)
    max_p = None
    ve = []
    for i in range(0, len(m[0])):
        f = k[0]
        for j in range(0, len(m)):
            f += m[j][i]
        # print(f, y[i], y[i]-f)
        ve.append(y[i]-f)
        if max_p is None:
            max_p = abs(y[i]-f)
        elif max_p < abs(y[i]-f):
            max_p = abs(y[i]-f)

    print(ve)
    print(f'w^2 = {check_symmetry(ve)}')
    
    # primer = [20, 18, -2, 34, 25, -17, 24, 42, 16, 26, 13, -23, 35, 21, 19, 8, 27, 11, -5, 7]
    # print(check_symmetry(primer))
    return


if __name__ == '__main__':
    main()
