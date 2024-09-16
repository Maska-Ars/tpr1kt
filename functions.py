import math


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
    return x**(1/3)


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
    return math.e**(a*x)


def e_pow_2(x):
    return math.e**(x**2)


def e1(x):
    return 1 / (1 + e_pow(x))


def e2(x):
    return (e_pow(x) - 1) / (e_pow(x) + 1)


def e3(x):
    return (e_pow(x) - e_pow(x, -1)) / 2


def calculate(l: list[float]) -> list[list[float]]:
    m = [[pow_2(x) for x in l]]
    m += [pow_3(x) for x in l]
    m += [pow_negative_1(x) for x in l]
    m += [pow_negative_2(x) for x in l]
    m += [pow_negative_3(x) for x in l]
    m += [kbrt(x) for x in l]
    m += [ln(x) for x in l]
    m += [sqrt(x) for x in l]
    m += [sin(x) for x in l]
    m += [tg(x) for x in l]
    m += [arctg(x) for x in l]
    m += [e_pow(x) for x in l]
    m += [e_pow_2(x) for x in l]
    m += [e1(x) for x in l]
    m += [e2(x) for x in l]
    m += [e3(x) for x in l]
    return m