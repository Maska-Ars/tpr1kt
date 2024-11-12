from functions import pair_correlation
from conversion import json_to_dict, dict_to_json
import json
from decimal import Decimal
from copy import deepcopy


def calculate_pair_correlation(infile: str = 'func_y3.json', outfile: str = 'pair_correlation.json') -> None:
    data = json_to_dict(infile)
    data = data['x']
    xn = list(data.keys())
    pair_cor = {}

    for x in xn:
        pair_cor.setdefault(x, {})

    for i in range(0, len(xn)):
        for j in range(0, len(xn)):
            if i == j:
                continue
            cor = pair_correlation(data[xn[i]], data[xn[j]])
            print(f'{xn[i]} {xn[j]}: {cor}')
            pair_cor[xn[i]].setdefault(xn[j], str(cor))

    with open(outfile, 'w+') as file:
        json.dump(pair_cor, file, indent=2)

    return None


def first_stage():
    calculate_pair_correlation()
    with open('pair_correlation.json', 'r') as f:
        data = json.load(f)
    for key1 in data.keys():
        for key2 in data[key1].keys():
            data[key1][key2] = Decimal(data[key1][key2])

    k_cor = 0
    for key1 in data.keys():
        for key2 in data[key1].keys():
            k_cor += 1
            if abs(data[key1][key2]) > 0.8:
                max_cor = data[key1][key2]
                max_pair = f'{key1} {key2}'
                print(max_pair, max_cor)
    print(k_cor)
    print()

    dep_data = {}
    for i in range(50, 100, 5):
        k = 0
        indep_k = 0
        all_indep = []
        for key1 in data.keys():

            dep = []
            indep = []
            dep_data.setdefault(key1, {})
            for key2 in data[key1].keys():
                if abs(data[key1][key2]) > i / 100:
                    k += 1
                    dep.append(key2)
                else:
                    indep.append(key2)
            dep_data[key1].setdefault('dep', dep)
            dep_data[key1].setdefault('indep', indep)
            if len(dep) == 1 and dep[0] == key1:
                indep_k += 1
                all_indep.append(key1)

        print(f'i = {i/100}, k = {k}, indep_k = {indep_k}')
        print(set(all_indep))


def gen_all_models(k: float = 0.95, n: int | None = None) -> list[list[str]]:
    with open('pair_correlation.json', 'r') as f:
        data = json.load(f)

    for key1 in data.keys():
        for key2 in data[key1].keys():
            data[key1][key2] = Decimal(data[key1][key2])

    indep_k = 0
    all_indep = []
    dep_data = {}
    for key1 in data.keys():
        dep = []
        indep = []
        dep_data.setdefault(key1, {})

        for key2 in data[key1].keys():
            if abs(data[key1][key2]) > k:
                dep.append(key2)
            else:
                indep.append(key2)

        dep_data[key1].setdefault('dep', dep)
        dep_data[key1].setdefault('indep', indep)
        if len(dep) == 1:
            indep_k += 1
            all_indep.append(key1)

    print(f'k = {k}, indep_k = {indep_k}')
    print(all_indep)

    l = []

    def r(vx: list, temp: list, max_len_l: int | None):
        if max_len_l is not None and len(l) == max_len_l:
            return

        if len(vx) == 0:
            l.append(temp + all_indep)
            return

        t = vx[0]
        copy_vx = deepcopy(vx)

        copy_vx.remove(t)

        copy_temp = deepcopy(temp)
        copy_temp.append(t)

        dep = set(dep_data[t]['dep']) - {t}

        new_vx = list(deepcopy(set(copy_vx)) - dep)

        r(new_vx, copy_temp, max_len_l)

        for el in dep:
            t = el

            copy_vx = deepcopy(vx)

            if t in copy_vx:
                copy_vx.remove(t)

            copy_temp = deepcopy(temp)
            copy_temp.append(t)

            el_dep = set(dep_data[t]['dep']) - {t}

            new_vx = list(deepcopy(set(copy_vx)) - el_dep)

            r(new_vx, copy_temp, max_len_l)

    for key in all_indep:
        data.pop(key)
        dep_data.pop(key)

    r(list(data.keys()), [], n)

    return l


if __name__ == '__main__':
    # first_stage()
    l = gen_all_models(0.7, 10)

    for vx in l:
        print(len(vx), sorted(vx))