"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit
from random import sample


# функция из задания: цикл с append-ом
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# list comprehension
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# 1-е место по скорости: использование встроенной функции циклического перебора (итератора)
def func_3(nums):
    new_arr = [key for key, val in enumerate(nums) if not val % 2]
    return new_arr


# самый медленный вариант с использованием встроенных функций filter
# и map, а также анонимных функций lambda
def func_4(nums):
    nums_even = list(filter(lambda x: x % 2 == 0, nums))
    return list(map(lambda x: nums.index(x), nums_even))


num_list = sample(range(1, 100000), 300)


print(timeit('func_1(num_list)', number=50000, globals=globals()))  # 1.1390022999839857
print(timeit('func_2(num_list)', number=50000, globals=globals()))  # 0.9164092999417335
print(timeit('func_3(num_list)', number=50000, globals=globals()))  # 0.882379199960269
print(timeit('func_4(num_list)', number=50000, globals=globals()))  # 13.839463700074703
# print(num_list)
# print(func_1(num_list))
# print(func_2(num_list))
# print(func_3(num_list))
# print(func_4(num_list))
