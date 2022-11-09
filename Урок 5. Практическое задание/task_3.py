"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
from timeit import timeit
from random import randint

any_lst = [randint(1, 10 ** 3) for i in range(10 ** 3)]
any_deque = deque([randint(1, 10 ** 3) for y in range(10 ** 3)])

# print(timeit('any_lst', globals=globals()))
# print(timeit('any_deque', globals=globals()))
# 0.018461199999933342
# 0.028432399999928748


"""
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
"""


def append_func(lst):
    for i in range(10 ** 4):
        lst.append(i)
    return lst


# print(timeit('append_func(any_lst.copy())', globals=globals(), number = 10000))
# print(timeit('append_func(any_deque.copy())', globals=globals(), number = 10000))
# 4.7363029000002825
# 5.01035580000007


def pop_func(lst):
    for i in range(10 ** 2):
        lst.pop()
    return lst

# print(timeit('pop_func(any_lst.copy())', globals=globals(), number=100000))
# print(timeit('pop_func(any_deque.copy())', globals=globals(), number=100000))
# 0.6030976000001829
# 0.9756888000001709


def extend_func(lst):
    for i in range(10 ** 2):
        lst.extend([y for y in range(100)])
    return lst

# print(timeit('extend_func(any_lst.copy())', globals=globals(), number=10000))
# print(timeit('extend_func(any_deque.copy())', globals=globals(), number=10000))
# 2.845627400000012
# 3.5206373000000895

# быстрее список


"""
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
"""

def appendleft_lst(lst):
    for i in range (10 ** 2):
        lst.insert(0, i)
    return lst

def appendleft_deq(deq):
    for i in range (10 ** 2):
        deq.appendleft(i)
    return deq

# print(timeit('appendleft_lst(any_lst)', globals=globals(), number=1000))
# print(timeit('appendleft_deq(any_deque)', globals=globals(), number=1000))
# 1.93539520000013
# 0.004396500000439119


def popleft_lst(lst):
    for i in range (10 ** 2):
        lst.pop(0)
    return lst

def popleft_deq(deq):
    for i in range (10 ** 2):
        deq.popleft()
    return deq

# print(timeit('popleft_lst(any_lst.copy())', globals=globals(), number=100000))
# print(timeit('popleft_deq(any_deque.copy())', globals=globals(), number=100000))
# 1.5532344000002922
# 0.9500217000004341


def extendleft_lst(lst):
    for i in range (10 ** 2):
        lst.insert(0, [randint(0, 100) for y in range (10)])
    return lst

def extendleft_deq(deq):
    for i in range(10 ** 2):
        deq.extendleft([randint(0, 100) for y in range (10)])
    return deq

# print(timeit('extendleft_lst(any_lst)', globals=globals(), number=10000))
# print(timeit('extendleft_deq(any_deque)', globals=globals(), number=10000))
# 306.3379541999984
# 6.198949799998445

# ДЕК быстрее по операциям: appendleft, popleft, extendleft
"""

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

def get_func(lst):
    for i in range(10 ** 3):
        a = lst[i]

# print(timeit('get_func(any_lst)', globals=globals(), number=100000))
# print(timeit('get_func(any_deque)', globals=globals(), number=100000))
# 3.1256184999983816
# 4.062625099999423

# Получение элемента из списка быстрее, чем из дека