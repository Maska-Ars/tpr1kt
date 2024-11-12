from functions import pair_correlation
from conversion import json_to_dict, dict_to_json
import json
from decimal import Decimal


def cor_model(vx: list[str], k: float = 0.15, file: str = 'func_y3.json') -> list[str]:
    data = json_to_dict(file)

    d = []
    for x in vx:
        if abs(pair_correlation(data['x'][x], data['y']['y3'])) >= k:
            d.append(x)

    return d

