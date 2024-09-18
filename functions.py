import math
import decimal
from statistics import StatisticsError
from decimal import Decimal

decimal.getcontext().prec = 16


def pow_2(x):
    return x**2


def pow_3(x):
    return x**3


def pow_negative_1(x):
    return 1/x


def pow_negative_2(x):
    return 1 / x**2


def pow_negative_3(x):
    return 1 / x**3


def kbrt(x):
    return x**(Decimal(1/3))


def ln(x):
    return math.log(x, math.e)


def sqrt(x):
    return math.sqrt(x)


def sin(x):
    return math.sin(x)


def tg(x):
    return math.tan(x)


def arctg(x):
    return math.atan(x)


def e_pow(x, a=0):
    return Decimal(a*x).exp()


def e_pow_2(x):
    return Decimal(x**2).exp()


def e1(x):
    return 1 / (1 + e_pow(x))


def e2(x):
    return (e_pow(x) - 1) / (e_pow(x) + 1)


def e3(x):
    return (e_pow(x) - e_pow(x, -1)) / 2


def calculate(l: list[float]) -> list[list[float]]:
    m = [[pow_2(x) for x in l]]
    m += [[pow_3(x) for x in l]]
    m += [[pow_negative_1(x) for x in l]]
    m += [[pow_negative_2(x) for x in l]]
    m += [[pow_negative_3(x) for x in l]]
    m += [[kbrt(x) for x in l]]
    m += [[ln(x) for x in l]]
    m += [[sqrt(x) for x in l]]
    m += [[sin(x) for x in l]]
    m += [[tg(x) for x in l]]
    m += [[arctg(x) for x in l]]
    m += [[e_pow(x) for x in l]]
    m += [[e_pow_2(x) for x in l]]
    m += [[e1(x) for x in l]]
    m += [[e2(x) for x in l]]
    m += [[e3(x) for x in l]]
    return m


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
    except ZeroDivisionError:
        raise StatisticsError('at least one of the inputs is constant')
