"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для третьего скрипта
Курс Алгоритмы и структуры Python: Урок 4, задание 1
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

"""
from timeit import timeit
from random import sample
from memory_profiler import profile
from pympler import asizeof


# функция из задания: цикл с append-ом
@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# list comprehension
@profile
def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# 1-е место по скорости: использование встроенной функции циклического перебора (итератора)
@profile
def func_3(nums):
    new_arr = [key for key, val in enumerate(nums) if not val % 2]
    return new_arr


# самый медленный вариант с использованием встроенных функций filter
# и map, а также анонимных функций lambda
@profile
def func_4(nums):
    nums_even = list(filter(lambda x: x % 2 == 0, nums))
    return list(map(lambda x: nums.index(x), nums_even))


"""
AFTER optimization
использование генератора, т.к. генератор занимает в разы меньше памяти,
чем список:
6296 -- > 816

По profile видно разницу по количеству вхождений (Occurances)
"""

@profile
def func_5(nums):
    new_gen = (key for key, val in enumerate(nums) if not val % 2)
    return new_gen


num_list = sample(range(1, 100000), 300)
func_1(num_list)
func_2(num_list)
func_3(num_list)
func_4(num_list)
func_5(num_list)
print(f'Исп.память под func_1 - {asizeof.asizeof(func_1(num_list))}')
print(f'Исп.память под func_2 - {asizeof.asizeof(func_2(num_list))}')
print(f'Исп.память под func_3 - {asizeof.asizeof(func_3(num_list))}')
print(f'Исп.память под func_4 - {asizeof.asizeof(func_4(num_list))}')
print(f'Исп.память под func_5 (оптимизация) - {asizeof.asizeof(func_5(num_list))}')


