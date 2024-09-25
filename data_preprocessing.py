from decimal import Decimal, getcontext
from functions import calculate, correlation

getcontext().prec = 64


def step1(x: list[Decimal]) -> list[Decimal]:
    """
    1 шаг алгоритма
    :param x: вектор значений управляющего фактора;
    :return: Возвращает вектор значений x преобразованный на отрезок [2, 102]
    """
    m = max(x)
    return [2 + i / m * 100 for i in x]


def step2(x: list[Decimal], y: list[Decimal]) -> tuple[Decimal, list[Decimal], str]:
    """
    2 шаг алгоритма
    :param x: вектор значений управляющего фактора на отрезке [2, 102];
    :param y: вектор значений управляемого фактора;
    :return: Возвращает максимальный модуль коэффициента корреляции Пирсона, новый вектор значений и имя функции
    """
    vfx, name_functions = calculate(x)
    vr = []
    for i in range(0, len(vfx)):
        vr.append(abs(correlation(vfx[i], y)))
    rmax = max(vr)
    imax = vr.index(rmax)
    return max(vr), vfx[imax], name_functions[imax]


def step3(x: list[Decimal],
          y: list[Decimal],
          rmax: Decimal,
          fx: list[Decimal],
          e: Decimal = Decimal(0.01)) -> tuple[list[Decimal], bool]:
    """
    3 шаг алгоритма
    :param x: вектор значений управляющего фактора на отрезке [2, 102];
    :param y: вектор значений управляемого фактора;
    :param rmax: максимальный модуль коэффициента корреляции Пирсона;
    :param fx: вектор значений управляющего фактора при rmax;
    :param e: минимальное значение;
    :return: Возвращает измененный вектор значений управляющего фактора и флаг True-изменен, False-нет.
    """
    if rmax > correlation(x, y) + e:
        return fx, True
    return x, False


def run(x: list[Decimal],
        y: list[Decimal],
        i: int = 2) -> tuple[list[Decimal], list[str]]:
    flag = True
    vf = []
    while flag and i > 0:
        x = step1(x)
        # print('step1')
        rmax, fx, name_func = step2(x, y)
        # print('step2')
        new_x, flag = step3(x, y, rmax, fx)
        if flag:
            x = new_x
            vf.append(name_func)
        # print('step3', name_func)
        i -= 1

    return x, vf
