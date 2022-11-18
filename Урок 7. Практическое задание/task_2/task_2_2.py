"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def median_search(lst):
    num = int((len(lst) - 1) / 2)
    for i in range(num):
        lst.pop(lst.index(max(lst)))

    return max(lst)


if __name__ == '__main__':
    m = [10, 100, 1000]
    for el in m:
        rand_lst = [randint(-10000, 10000) for i in range(2*el + 1)]
        # print(rand_lst)
        # print(median_search(rand_lst))
        print(f"for m = {el} time = {timeit('median_search(rand_lst)', globals=globals(), number=10000)}")


"""
for m = 10 time = 0.023839400033466518
for m = 100 time = 0.02225530007854104
for m = 1000 time = 0.2526956999208778
"""
