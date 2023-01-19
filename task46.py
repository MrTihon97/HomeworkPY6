# Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
from random import randint

arr = [randint(1, 10) for i in range(5)]
sum = []
middle = len(arr)//2 + len(arr)%2
for i in range(middle):
        sum.append(arr[i] * arr[len(arr) - i - 1])
print(arr, '=>', (sum))


