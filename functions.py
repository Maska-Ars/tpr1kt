import math
import decimal
from statistics import StatisticsError
from decimal import Decimal

decimal.getcontext().prec = 64  # Количество цифр после запятой

soft_func_to_math_func = {
    'pow_2': 'x^2',
    'pow_3': 'x^3',
    'pow_negative_1': '1/x',
    'pow_negative_2': '1/x^2',
    'pow_negative_3': '1/x^3',
    'kbrt': 'x^(1/3)',
    'ln': 'ln(x)',
    'sqrt': 'x^(1/2)',
    'sin': 'sin(x)',
    'tg': 'tg(x)',
    'arctg': 'arctg(x)',
    'e_pow': 'e^x',
    'e_pow_2': 'e^(x^2)',
    'e1': '1/(1+e^x)',
    'e2': '(e^x-1)/(e^x+1)',
    'e3': '(e^x-e^(-x))/2'
}


def pow_2(x: Decimal) -> Decimal:
    return x**2


def pow_3(x: Decimal) -> Decimal:
    return x**3


def pow_negative_1(x: Decimal) -> Decimal:
    return 1/x


def pow_negative_2(x: Decimal) -> Decimal:
    return 1 / x**2


def pow_negative_3(x: Decimal) -> Decimal:
    return 1 / x**3


def kbrt(x: Decimal) -> Decimal:
    return x**(Decimal(1/3))


def ln(x: Decimal) -> Decimal:
    return x.ln()


def sqrt(x: Decimal) -> Decimal:
    return x.sqrt()


def sin(x: Decimal) -> Decimal:
    return Decimal(math.sin(x))


def tg(x: Decimal) -> Decimal:
    return Decimal(math.tan(x))


def arctg(x: Decimal) -> Decimal:
    return Decimal(math.atan(x))


def e_pow(x: Decimal, a=1) -> Decimal:
    return Decimal(a*x).exp()


def e_pow_2(x: Decimal) -> Decimal:
    return Decimal(x**2).exp()


def e1(x: Decimal) -> Decimal:
    return Decimal(1) / (Decimal(1) + e_pow(x))


def e2(x: Decimal) -> Decimal:
    return (e_pow(x) - 1) / (e_pow(x) + 1)


def e3(x: Decimal) -> Decimal:
    return (e_pow(x) - e_pow(x, -1)) / 2


def calculate(vx: list[Decimal]) -> tuple[list[list[Decimal]], list[str]]:
    m = [[pow_2(x) for x in vx]]
    m += [[pow_3(x) for x in vx]]
    m += [[pow_negative_1(x) for x in vx]]
    m += [[pow_negative_2(x) for x in vx]]
    m += [[pow_negative_3(x) for x in vx]]
    m += [[kbrt(x) for x in vx]]
    m += [[ln(x) for x in vx]]
    m += [[sqrt(x) for x in vx]]
    m += [[sin(x) for x in vx]]
    m += [[tg(x) for x in vx]]
    m += [[arctg(x) for x in vx]]
    m += [[e_pow(x) for x in vx]]
    m += [[e_pow_2(x) for x in vx]]
    m += [[e1(x) for x in vx]]
    m += [[e2(x) for x in vx]]
    m += [[e3(x) for x in vx]]
    return m, ['pow_2',
               'pow_3',
               'pow_negative_1',
               'pow_negative_2',
               'pow_negative_3',
               'kbrt',
               'ln',
               'sqrt',
               'sin',
               'tg',
               'arctg',
               'e_pow',
               'e_pow_2',
               'e1',
               'e2',
               'e3'
               ]


def sumprod(p: list[Decimal], q: list[Decimal]) -> Decimal:
    temp = Decimal(0)
    for i in range(0, len(p)):
        temp += p[i] * q[i]
    return temp


def correlation(x, y, /, *, method='linear'):
    n = len(x)
    if len(y) != n:
        raise StatisticsError('correlation requires that both inputs have same number of data points')
    if n < 2:
        raise StatisticsError('correlation requires at least two data points')
    if method not in {'linear', 'ranked'}:
        raise ValueError(f'Unknown method: {method!r}')
    if method == 'ranked':
        raise ValueError('Идите на #$*!')
    else:
        xbar = Decimal(sum(x) / n)
        ybar = Decimal(sum(y) / n)

        x = [Decimal(xi) - xbar for xi in x]
        y = [Decimal(yi) - ybar for yi in y]

    sxy = sumprod(x, y)
    sxx = sumprod(x, x)
    syy = sumprod(y, y)

    try:
        return sxy / Decimal(sqrt(sxx * syy))
    except decimal.InvalidOperation:
        print(x)
        print(sxy, sxx, syy)
        raise StatisticsError('Опять что-то на ноль поделилось')
    except ZeroDivisionError:
        raise StatisticsError('at least one of the inputs is constant')


def pair_correlation(x1: list[Decimal], x2: list[Decimal]):
    x1bar = Decimal(sum(x1) / len(x1))
    x2bar = Decimal(sum(x2) / len(x2))

    x1 = [xi - x1bar for xi in x1]
    x2 = [yi - x2bar for yi in x2]

    sx1x2 = sumprod(x1, x2)
    sx1 = sum([Decimal(x**2) for x in x1])
    sx2 = sum([Decimal(x**2) for x in x2])

    return sx1x2 / sqrt(sx1 * sx2)


def pairwise_product(data: dict[str, dict[str, list]]) -> dict[str, dict[str, list]]:
    d = {'x': data['x'], 'y': data['y']}
    mx = list(data['x'].keys())
    for i in range(0, len(mx)):
        x1 = mx[i]
        vx1 = data['x'][x1]
        for j in range(i+1, len(mx)):
            x2 = mx[j]
            vx2 = data['x'][x2]
            v = []
            for i in range(0, len(vx1)):
                v.append(vx1[i] * vx2[i])
            d['x'].setdefault(f'{x1}*{x2}', v)

    for key in data['x'].keys():
        for i in range(0, len(data['x'][key])):
            data['x'][key][i] = str(data['x'][key][i])

    for key in data['y'].keys():
        for i in range(0, len(data['y'][key])):
            data['y'][key][i] = str(data['y'][key][i])

    return d