"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


# сортировка Шелла
def shell_sort(lst):
    n = len(lst)
    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            temp = lst[i]
            j = i
            while j >= interval and lst[j - interval] > temp:
                lst[j] = lst[j - interval]
                j -= interval

            lst[j] = temp
        interval //= 2
    return lst


def median_search(lst):
    lst = shell_sort(lst)
    return lst[int((len(lst)-1)/2)]


if __name__ == '__main__':
    m = [10, 100, 1000]
    for el in m:
        rand_lst = [randint(-100, 100) for i in range(2*el + 1)]
        print(f'm={el} - {timeit("median_search(rand_lst)", globals=globals(), number=10000)}')


"""
m=10 - 0.2184666000539437
m=100 - 5.006028800038621
m=1000 - 68.96946449996904
"""
