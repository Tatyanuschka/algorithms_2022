"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение мемоизацией
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!

П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint
from cProfile import run
from memory_profiler import profile


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=100000))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=100000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=100000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=100000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=100000))


def main():
    recursive_reverse(num_100)
    recursive_reverse(num_1000)
    recursive_reverse(num_10000)
    recursive_reverse_mem(num_100)
    recursive_reverse_mem(num_1000)
    recursive_reverse_mem(num_10000)

def cycle_main():
    for i in range(10000):
        main()

run('cycle_main()')

#  По скорости быстрее функция, декорированная мемоизацией,
# но предполагаю, что кэш-словарь будет занимать значительную область оперативной памяти

# """
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     52     20.2 MiB     20.2 MiB           1       def decorate(*args):
#     53
#     54     20.2 MiB      0.0 MiB           1           if args in cache:
#     55     20.2 MiB      0.0 MiB           1               return cache[args]
#     56                                                 else:
#     57                                                     cache[args] = f(*args)
#     58                                                     return cache[args]
#
#
# Filename: C:\Users\tatya\OneDrive\Documents\GeekBrains\Python\Алгоритмы_Структуры\Домашка\Урок 4. Практическое задание\task_2.py
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     52     20.2 MiB     20.2 MiB           1       def decorate(*args):
#     53
#     54     20.2 MiB      0.0 MiB           1           if args in cache:
#     55     20.2 MiB      0.0 MiB           1               return cache[args]
#     56                                                 else:
#     57                                                     cache[args] = f(*args)
#     58                                                     return cache[args]
#
#
# Filename: C:\Users\tatya\OneDrive\Documents\GeekBrains\Python\Алгоритмы_Структуры\Домашка\Урок 4. Практическое задание\task_2.py
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     52     20.2 MiB     20.2 MiB           1       def decorate(*args):
#     53
#     54     20.2 MiB      0.0 MiB           1           if args in cache:
#     55     20.2 MiB      0.0 MiB           1               return cache[args]
#     56                                                 else:
#     57                                                     cache[args] = f(*args)
#     58                                                     return cache[args]
#
#
# Filename: C:\Users\tatya\OneDrive\Documents\GeekBrains\Python\Алгоритмы_Структуры\Домашка\Урок 4. Практическое задание\task_2.py
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     52     20.2 MiB     20.2 MiB           1       def decorate(*args):
#     53
#     54     20.2 MiB      0.0 MiB           1           if args in cache:
#     55     20.2 MiB      0.0 MiB           1               return cache[args]
#     56                                                 else:
#     57                                                     cache[args] = f(*args)
#     58                                                     return cache[args]
#
#
# Filename: C:\Users\tatya\OneDrive\Documents\GeekBrains\Python\Алгоритмы_Структуры\Домашка\Урок 4. Практическое задание\task_2.py
#
# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#     52     20.2 MiB     20.2 MiB           1       def decorate(*args):
#     53
#     54     20.2 MiB      0.0 MiB           1           if args in cache:
#     55     20.2 MiB      0.0 MiB           1               return cache[args]
#     56                                                 else:
#     57                                                     cache[args] = f(*args)
#     58                                                     return cache[args]
#
#
#          15290004 function calls (15040004 primitive calls) in 78.790 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1440000    0.635    0.000    1.029    0.000 <string>:1(<lambda>)
#         1    0.000    0.000   78.790   78.790 <string>:1(<module>)
#     30000    0.080    0.000    0.087    0.000 contextlib.py:102(__init__)
#     30000    0.038    0.000    0.242    0.000 contextlib.py:130(__enter__)
#     30000    0.150    0.000    0.503    0.000 contextlib.py:139(__exit__)
#     30000    0.044    0.000    0.131    0.000 contextlib.py:279(helper)
#     30000    0.057    0.000    0.296    0.000 coroutines.py:164(iscoroutinefunction)
#     30000    0.021    0.000    0.027    0.000 functools.py:421(_unwrap_partial)
#     60000    0.117    0.000    7.505    0.000 genericpath.py:16(exists)
#     30000    0.048    0.000    0.048    0.000 inspect.py:1049(__init__)
#   1440000    1.205    0.000    1.205    0.000 inspect.py:1059(tokeneater)
#     30000    2.427    0.000   13.408    0.000 inspect.py:1109(getblock)
#     30000    0.282    0.000   21.742    0.001 inspect.py:1120(getsourcelines)
#    120000    0.097    0.000    0.137    0.000 inspect.py:182(ismodule)
#     60000    0.030    0.000    0.041    0.000 inspect.py:191(isclass)
#     90000    0.053    0.000    0.084    0.000 inspect.py:199(ismethod)
#     90000    0.050    0.000    0.064    0.000 inspect.py:277(isfunction)
#     30000    0.113    0.000    0.199    0.000 inspect.py:290(_has_code_flag)
#     30000    0.026    0.000    0.225    0.000 inspect.py:308(iscoroutinefunction)
#     90000    0.046    0.000    0.061    0.000 inspect.py:355(istraceback)
#     90000    0.043    0.000    0.057    0.000 inspect.py:365(isframe)
#     90000    0.053    0.000    0.074    0.000 inspect.py:379(iscode)
#     30000    0.109    0.000    0.170    0.000 inspect.py:612(unwrap)
#     30000    0.022    0.000    0.035    0.000 inspect.py:629(_is_wrapper)
#     30000    0.133    0.000    0.321    0.000 inspect.py:773(getfile)
#     30000    0.241    0.000    3.888    0.000 inspect.py:813(getsourcefile)
#     90000    0.058    0.000    0.092    0.000 inspect.py:820(<genexpr>)
#     90000    0.037    0.000    0.051    0.000 inspect.py:823(<genexpr>)
#     30000    0.106    0.000    0.174    0.000 inspect.py:850(getmodule)
#     30000    0.439    0.000    7.815    0.000 inspect.py:932(findsource)
#     60000    0.089    0.000    0.104    0.000 linecache.py:36(getlines)
#     30000    0.142    0.000    2.890    0.000 linecache.py:52(checkcache)
#     30000    0.269    0.000   78.367    0.003 memory_profiler.py:1183(wrapper)
#     30000    0.247    0.000    0.343    0.000 memory_profiler.py:1199(choose_backend)
#    180000    0.065    0.000    0.065    0.000 memory_profiler.py:1213(<genexpr>)
#     30000    0.043    0.000    0.043    0.000 memory_profiler.py:638(__init__)
#     30000    0.348    0.000   26.567    0.001 memory_profiler.py:643(add)
#     60000    0.086    0.000    0.086    0.000 memory_profiler.py:687(items)
#    240000    0.149    0.000    0.200    0.000 memory_profiler.py:693(<genexpr>)
#     30000    0.180    0.000    0.591    0.000 memory_profiler.py:700(__init__)
#     30000    0.152    0.000   27.162    0.001 memory_profiler.py:711(__call__)
#     30000    0.069    0.000   26.637    0.001 memory_profiler.py:726(add_function)
#     60000    0.114    0.000    0.480    0.000 memory_profiler.py:738(_count_ctxmgr)
#     30000    0.052    0.000    0.348    0.000 memory_profiler.py:746(wrap_function)
#     30000    0.371    0.000    5.549    0.000 memory_profiler.py:757(f)
#     30000    0.052    0.000    0.148    0.000 memory_profiler.py:773(enable_by_count)
#     30000    0.157    0.000    0.218    0.000 memory_profiler.py:780(disable_by_count)
#     30000    0.075    0.000    0.096    0.000 memory_profiler.py:840(enable)
#     30000    0.049    0.000    0.062    0.000 memory_profiler.py:847(disable)
#     30000    0.821    0.000   44.796    0.001 memory_profiler.py:851(show_results)
#     30000    0.025    0.000    0.127    0.000 re.py:249(compile)
#     30000    0.057    0.000    0.102    0.000 re.py:288(_compile)
# 280000/30000    0.267    0.000    0.267    0.000 task_2.py:21(recursive_reverse)
#     30000    4.302    0.000    4.302    0.000 task_2.py:52(decorate)
#     10000    0.141    0.000   78.775    0.008 task_2.py:87(main)
#         1    0.015    0.015   78.790   78.790 task_2.py:95(cycle_main)
#   1470000    5.598    0.000    9.707    0.000 tokenize.py:431(_tokenize)
#     30000    0.020    0.000    0.020    0.000 tokenize.py:614(generate_tokens)
#   1440000    0.394    0.000    0.394    0.000 {built-in method __new__ of type object at 0x00007FFC2693B920}
#     60000    0.076    0.000    0.220    0.000 {built-in method builtins.any}
#         1    0.001    0.001   78.790   78.790 {built-in method builtins.exec}
#     90000    0.028    0.000    0.028    0.000 {built-in method builtins.getattr}
#     90000    0.038    0.000    0.038    0.000 {built-in method builtins.hasattr}
#     30000    0.016    0.000    0.016    0.000 {built-in method builtins.id}
#    690000    0.196    0.000    0.196    0.000 {built-in method builtins.isinstance}
#     30000    0.012    0.000    0.012    0.000 {built-in method builtins.iter}
#    420000    0.089    0.000    0.089    0.000 {built-in method builtins.len}
#     60000    0.077    0.000    0.557    0.000 {built-in method builtins.next}
#     90000   10.125    0.000   10.125    0.000 {built-in method nt.stat}
#     30000    0.011    0.000    0.011    0.000 {built-in method sys.getrecursionlimit}
#     30000    0.009    0.000    0.009    0.000 {built-in method sys.gettrace}
#     60000    0.026    0.000    0.026    0.000 {built-in method sys.settrace}
#    150000    0.047    0.000    0.047    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    150000    0.076    0.000    0.076    0.000 {method 'endswith' of 'str' objects}
#    450000    0.787    0.000    0.787    0.000 {method 'format' of 'str' objects}
#    360000    0.093    0.000    0.093    0.000 {method 'get' of 'dict' objects}
#     30000    0.012    0.000    0.012    0.000 {method 'insert' of 'list' objects}
#   1020000    0.185    0.000    0.185    0.000 {method 'isidentifier' of 'str' objects}
#   1230000    2.663    0.000    2.663    0.000 {method 'match' of 're.Pattern' objects}
#     30000    0.018    0.000    0.018    0.000 {method 'pop' of 'list' objects}
#   1200000    0.253    0.000    0.253    0.000 {method 'span' of 're.Match' objects}
#     30000    0.018    0.000    0.018    0.000 {method 'update' of 'dict' objects}
#    330000   42.828    0.000   42.828    0.000 {method 'write' of '_io.TextIOWrapper' objects}
#
# """


