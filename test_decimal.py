from decimal import Decimal, getcontext
from functions import e3, pow_negative_3
from threading import Thread
getcontext().prec = 64


l = [Decimal(i) for i in range(0, 11)]
print(type(sum(l)))

d = Decimal('86.22123886608438532665426833080236913636389919075940444425670243')
