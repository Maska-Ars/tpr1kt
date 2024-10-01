from decimal import Decimal, getcontext
from functions import calculate, correlation
from threading import Thread

getcontext().prec = 64


def step1(x: list[Decimal]) -> list[Decimal]:
    """
    1 шаг алгоритма
    :param x: вектор значений управляющего фактора;
    :return: Возвращает вектор значений x преобразованный на отрезок [2, 102]
    """
    sup = max(x)
    inf = min(x)

    return [2 + (i - inf) / (sup - inf) * 100 for i in x]


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
    """
    Запуск алгоритма
    :param x: вектор значений управляющего фактора на отрезке [2, 102];
    :param y: вектор значений управляемого фактора;
    :param i: максимальное количество проходов алгоритма;
    :return: Возвращает измененный вектор значений управляющего фактора и список примененных функций.
    """
    flag = True
    vf = []
    while flag and i > 0:
        x = step1(x)

        rmax, fx, name_func = step2(x, y)

        new_x, flag = step3(x, y, rmax, fx)
        if flag:
            x = new_x
            vf.append(name_func)

        i -= 1

    return x, vf


class AlgTh:
    """
    Класс для многопоточного запуска алгоритма
    """

    def __init__(self, data: dict):
        self.data = data

    def run(self,
            x: str,
            y: str,
            i: int = 2) -> None:
        vx = self.data['x'][x]
        vy = self.data['y'][y]

        vx, vf = run(vx, vy, i)

        self.data['x'][x] = vx
        self.data['functions'][x] = vf

        return None

    def run_all_in_threads(self, y: int, i: int = 2) -> dict:
        self.data.setdefault('functions', {})

        for x in self.data['x'].keys():
            self.data['functions'].setdefault(x, [])

        yn = f'y{y}'

        threads = []
        for x in self.data['x'].keys():
            thread = Thread(target=self.run, args=(x, yn, i))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for i in range(0, len(threads)):
            threads[i].join()
            print(i)

        return {
            'y': {f'{yn}': self.data['y'][yn]},
            'functions': self.data['functions'],
            'x': self.data['x']
            }

    def run_all_in_sync(self, y: int, i: int = 2) -> dict:
        self.data.setdefault('functions', {})

        for x in self.data['x'].keys():
            self.data['functions'].setdefault(x, [])

        yn = f'y{y}'

        for x in self.data['x'].keys():
            self.run(x, yn, i)
            print(f'{x} завершен')

        return self.data






















