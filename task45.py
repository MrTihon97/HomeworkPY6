# Найти сумму чисел списка стоящих на нечетной позиции
from random import randint
from functools import reduce

arr = [randint(1, 10) for i in range(10)]
odd = arr[1::2]
res = reduce(lambda a, b: a+b, odd)
print(f"На нечетных позициях: {odd} сумма: {res}")
