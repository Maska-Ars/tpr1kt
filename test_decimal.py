from decimal import Decimal, getcontext
from functions import e3, pow_negative_3
getcontext().prec = 64

x = Decimal()
print(x)
f = pow_negative_3(e3(x))
print(f)