"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

simple_dict = {i:i for i in range(10 ** 4)}
ord_dict = OrderedDict({i:i for i in range(10 ** 4)})

"""
Удаляем пару ключ: значение
операция выполняется быстрее в стандартном словаре
"""

def popitem_dict(dict):
    for i in range(100):
        dict.popitem()
    return dict

def popitem_od_lifo(ord_dict):
    for i in range(100):
        ord_dict.popitem(last=True)
    return ord_dict

# print(timeit('popitem_dict(simple_dict.copy())', globals=globals(), number=10000))
# print(timeit('popitem_od_lifo(ord_dict.copy())', globals=globals(), number=10000))
# 0.8472437999989779
# 7.27346899999975

"""
Изменение значений в словаре по ключу:
стандартный словарь работает быстрее, чем OrderedDict
"""

def change_val(dict):
    for i in range (len(dict)):
        dict[i] = i * 2
    return dict

# print(timeit('change_val(simple_dict)', globals=globals(), number=10000))
# print(timeit('change_val(ord_dict)', globals=globals(), number=10000))
# 7.752055000000837
# 10.219029600000795

"""
Получение значения по ключу и копирование их в список:
быстрее в стандартном словаре Python 3.10
"""

def get_val(dict):
    val_lst = []
    for key, val in dict.items():
        val_lst.append(val)
    return val_lst

# print(timeit('get_val(simple_dict)', globals=globals(), number=10000))
# print(timeit('get_val(ord_dict)', globals=globals(), number=10000))
# 5.5546863999989
# 8.381785200001104

"""
добавление пары ключ:значение в словари -->
работа функции со стандартным словарем быстрее
"""

def add_func(dict):
    for i in range(len(dict)+1, len(dict) + 100):
        dict[i] = i * 2
    return dict

# print(timeit('add_func(simple_dict)', globals=globals(), number=100000))
# print(timeit('add_func(ord_dict)', globals=globals(), number=100000))
# 1.5309338999995816
# 2.623916399999871