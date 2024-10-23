from functions import pair_correlation
from conversion import json_to_dict, dict_to_json
import json
from decimal import Decimal


def calculate_pair_correlation() -> None:
    data = json_to_dict('func_y3.json')
    data = data['x']
    xn = list(data.keys())
    pair_cor = {}

    for x in xn:
        pair_cor.setdefault(x, {})

    for i in range(0, len(xn)):
        for j in range(i+1, len(xn)):
            cor = pair_correlation(data[xn[i]], data[xn[j]])
            print(f'{xn[i]} {xn[j]}: {cor}')
            pair_cor[xn[i]].setdefault(xn[j], str(cor))

    with open('pair_correlation.json', 'w+') as file:
        json.dump(pair_cor, file, indent=2)

    return None


def first_stage():
    # calculate_pair_correlation()
    with open('pair_correlation.json', 'r') as f:
        data = json.load(f)
    for key1 in data.keys():
        for key2 in data[key1].keys():
            data[key1][key2] = Decimal(data[key1][key2])

    max_cor = 0
    max_pair = ''
    for key1 in data.keys():
        for key2 in data[key1].keys():
            if abs(data[key1][key2]) > 0.8:
                max_cor = data[key1][key2]
                max_pair = f'{key1} {key2}'

                print(max_pair, max_cor)


if __name__ == '__main__':
    first_stage()
