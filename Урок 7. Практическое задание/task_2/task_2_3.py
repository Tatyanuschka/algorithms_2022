"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

3) с помощью встроенной функции поиска медианы

сделайте замеры на массивах длиной 10, 100, 1000 элементов

В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from timeit import timeit
from random import randint
from statistics import median
from numpy import median as np_median


m = [10, 100, 1000]
for el in m:
    rand_lst = [randint(-10000, 10000) for i in range(2*el + 1)]
    # print(median(rand_lst))
    print(f"for m={el} in statistics time = {timeit('median(rand_lst)', globals=globals(), number=10000)}")
    # print(np_median(rand_lst))
    print(f"for m={el} in numpy time = {timeit('np_median(rand_lst)', globals=globals(), number=10000)}")


"""
for m=10 in statistics time = 0.006155700073577464
for m=10 in numpy time = 0.18725069996435195
for m=100 in statistics time = 0.06866360001731664
for m=100 in numpy time = 0.3412346000550315
for m=1000 in statistics time = 1.832646399969235
for m=1000 in numpy time = 1.7367178000276908
"""