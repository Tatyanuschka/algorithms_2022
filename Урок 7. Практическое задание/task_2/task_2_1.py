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


# гномья сортировка
def gnome_sort(lst):
    i, j, len_lst = 1, 2, len(lst)
    while i < len_lst:
        if lst[i - 1] <= lst[i]:
            i, j = j, j + 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst


if __name__ == '__main__':

    m = int(input('Введите число m - '))
    rand_lst = [randint(-100, 100) for _ in range(m * 2 + 1)]
    print(f"Сорт-ка Шелла - {timeit('shell_sort(rand_lst[:])[m]', globals=globals(), number=10000)}")
    print(f"Гномья сорт-ка - {timeit('gnome_sort(rand_lst[:])[m]', globals=globals(), number=10000)}")


"""
Введите число m - 10
Сорт-ка Шелла - 0.12067050009500235
Гномья сорт-ка - 0.2088970000622794

Введите число m - 100
Сорт-ка Шелла - 2.3972766998922452
Гномья сорт-ка - 19.177614799933508

Введите число m - 1000
Сорт-ка Шелла - 50.38286429992877
Гномья сортировка - очень долго (скорее всего ок. 40 мин)

при timeit (number=1000)
Введите число m - 1000
Сорт-ка Шелла - 4.486613600049168
Гномья сорт-ка - 234.62233789998572
"""
