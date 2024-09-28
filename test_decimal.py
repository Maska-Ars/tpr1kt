from decimal import Decimal, getcontext
from functions import e3, pow_negative_3
from threading import Thread
getcontext().prec = 64

def transform(x, a, b):
  """
  Преобразует число x с отрезка [a, b] на отрезок [2, 102].

  Args:
      x: Число, которое нужно преобразовать.
      a: Нижняя граница исходного отрезка.
      b: Верхняя граница исходного отрезка.

  Returns:
      Преобразованное число на отрезке [2, 102].
  """

  # Проверка, что x находится на отрезке [a, b]
  if x < a or x > b:
    raise ValueError("x не находится на отрезке [a, b]")

  # Линейное преобразование
  return (x - a) / (b - a) * (102 - 2) + 2

print(transform(-1, -1, 5))




d = Decimal('86.22123886608438532665426833080236913636389919075940444425670243')

print(d**(Decimal(1/3)))