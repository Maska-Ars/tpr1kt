import decimal
from decimal import Decimal
from functions import e3, pow_negative_3


if __name__ == '__main__':
    decimal.getcontext().prec = 8

    x = Decimal(224.2) * Decimal(33.9)
    print(str(x))
