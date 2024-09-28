import csv
import json
from decimal import Decimal


def read(file: str) -> list[list]:
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        return [line for line in reader]


def csv_to_dict(file: str) -> dict:

    l = read(file)
    l[0][0] = 'ГОД'

    l = [line[2:] for line in l[0:-46]]

    data = {'x': {}, 'y': {}, 'names': {}}

    for i in range(0, 17):
        data['names'].setdefault(f'x{i+1}', l[0][i])

    for i in range(17, 33):
        data['names'].setdefault(f'y{i-17+1}', l[0][i])

    for i in range(0, len(l)):
        for j in range(0, len(l[0])):
            l[i][j] = l[i][j].replace(' ', '')
            if ',' in l[i][j]:
                l[i][j] = l[i][j].replace(',', '.')
            try:
                float(l[i][j])
            except:
                pass

    for i in range(0, 17):
        values = []
        for j in range(1, len(l)):
            values.append(l[j][i])
        data['x'].setdefault(f'x{i+1}', values)
    for i in range(17, 33):
        values = []
        for j in range(1, len(l)):
            values.append(l[j][i])
        data['y'].setdefault(f'y{i-17+1}', values)

    return data


def dict_to_json(data: dict, file: str) -> None:

    for key in data['x'].keys():
        for i in range(0, len(data['x'][key])):
            data['x'][key][i] = str(data['x'][key][i])

    for key in data['y'].keys():
        for i in range(0, len(data['y'][key])):
            data['y'][key][i] = str(data['y'][key][i])

    with open(file, 'w+') as file:
        json.dump(data, file, indent=2)
    return None


def json_to_dict(file: str) -> dict[str, dict[str, list[Decimal]]]:

    with open(file, 'r') as f:
        data = json.load(f)

    for key in data['x'].keys():
        for i in range(0, len(data['x'][key])):
            data['x'][key][i] = Decimal(data['x'][key][i])

    for key in data['y'].keys():
        for i in range(0, len(data['y'][key])):
            data['y'][key][i] = Decimal(data['y'][key][i])

    return data
