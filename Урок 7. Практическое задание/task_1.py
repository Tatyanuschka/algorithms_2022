"""
Задание 1.

Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.

Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit


def bubble_sort(lst):

    cp_lst = lst.copy()
    n = 1

    while n < len(cp_lst):
        for i in range(len(cp_lst) - n):
            if cp_lst[i] < cp_lst[i + 1]:
                cp_lst[i+1], cp_lst[i] = cp_lst[i], cp_lst[i+1]

        n += 1
    return cp_lst


def bubble_sort_smart(lst):
    copy_lst = lst.copy()
    n = 1
    while n < len(copy_lst):
        flag = False
        for i in range(len(copy_lst) - n):
            if copy_lst[i] < copy_lst[i + 1]:
                copy_lst[i], copy_lst[i+1] = copy_lst[i+1], copy_lst[i]
                flag = True
        if not flag:
            break

        n += 1
    return copy_lst


rand_lst = [randint(-100, 100) for _ in range(100)]
rand_lst_sorted = [i for i in range(100, -100, -1)]  # изначально отсортиров.список

print(f'Исходный массив: \n{rand_lst}')
print(f'Отсортированный массив: \n{bubble_sort(rand_lst[:])}')
print(f'Отсортированный массив после оптимизации: \n{bubble_sort_smart(rand_lst[:])}')

print(f"Время bubble_sort - {timeit('bubble_sort(rand_lst[:])', globals=globals(), number=10000)}")
print(f"Время bubble_sort_smart - {timeit('bubble_sort_smart(rand_lst[:])', globals=globals(), number=10000)}")

print(f"Время bubble_sort на уже отсорт.списке - {timeit('bubble_sort(rand_lst_sorted[:])', globals=globals(), number=10000)}")
print(f"Время bubble_sort_smart на уже отсорт.списке - {timeit('bubble_sort_smart(rand_lst_sorted[:])', globals=globals(), number=10000)}")


"""
Время bubble_sort - 6.070837799925357
Время bubble_sort_smart - 5.769205500022508


Если список уже отсортирован, то доработка алгоритма пузырьковой сортировки
существенно оказывает влияние на время выполнения алгоритма
Время bubble_sort на уже отсорт.списке - 12.209748199908063
Время bubble_sort_smart на уже отсорт.списке - 0.13403810001909733
"""
