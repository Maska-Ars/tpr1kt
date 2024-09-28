from decimal import Decimal, getcontext  # Для работы с числами с заданной точностью
from functions import (
    pairwise_product
)  # Для расчетов

from data_preprocessing import run, AlgTh  # Для расчетов

from conversion import dict_to_json, json_to_dict, csv_to_dict  # Для сохранения и чтения данных

from time import time

# 17-32 болезни
# 0-16 параметры

getcontext().prec = 64  # Точность вычислений
print(Decimal('0.3')**20)


def main():
    # Чтение значений из csv
    data = csv_to_dict('Показатели 2005-2018 (24-01-20).csv')

    # Сохранение значений в json
    dict_to_json(data, 'data.json')

    # Чтение значений из json
    data = json_to_dict('data.json')

    # Добавление попарных произведений
    data = pairwise_product(data)

    # Сохранение значений и попарных произведений
    dict_to_json(data, 'data_pairwise_product.json')

    data = json_to_dict('data.json')
    # print(data)

    algth = AlgTh(data)
    t = time()
    data = algth.run_all_in_threads(1)
    print((time()-t)/60)

    dict_to_json(data, 'func.json')

    return


if __name__ == '__main__':
    main()
