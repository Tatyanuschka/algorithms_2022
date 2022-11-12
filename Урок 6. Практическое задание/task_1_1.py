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

Это файл для первого скрипта (курс "Основы Python, урок 4 задание 2)

Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
 (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.

"""

# BEFORE MEMORY OPTIMIZATION

from requests import get
from json import loads, dumps
from memory_profiler import profile, memory_usage
from recordclass import recordclass
from pympler import asizeof

# Проверяем использование памяти через profile

@profile
def currency_get():
    """function to get the list of names and values of all currencies for today"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    print(f'размер get.txt - {asizeof.asizeof((response))}')
    currency_rate = {}
    for el in response.split('<CharCode>')[1:]:
        currency_name = el.split('</CharCode>')[0]
        v = ((el.split('<Value>')[1]).split('</Value>')[0]).replace(',', '.')
        value = float(v)
        nominal = int(el.split('<Nominal>')[1].split('</Nominal')[0])
        currency_rate[currency_name] = (value, nominal)
    return currency_rate

@profile
def currency_rates(currency_name):
    """ function to print the value of certain currency"""
    currency_dict = currency_get()

    if currency_name in currency_dict.keys():
        print(f'Курс {currency_name} на сегодня равен {round(currency_dict[currency_name][0], 2)} руб. за {currency_dict[currency_name][1]}')
    else:
        print('Такой валюты не существует')

# проверяем использование памяти через декоратор с использованием memory_usage
def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

@decor
def currency_get2():
    """function to get the list of names and values of all currencies for today"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    print(f'размер get.txt - {asizeof.asizeof((response))}')
    currency_rate = {}
    for el in response.split('<CharCode>')[1:]:
        currency_name = el.split('</CharCode>')[0]
        v = ((el.split('<Value>')[1]).split('</Value>')[0]).replace(',', '.')
        value = float(v)
        nominal = int(el.split('<Nominal>')[1].split('</Nominal')[0])
        currency_rate[currency_name] = (value, nominal)
    return currency_rate

@decor
def currency_rates2(currency_name):
    """ function to print the value of certain currency"""
    currency_dict = currency_get()

    if currency_name in currency_dict.keys():
        print(f'Курс {currency_name} на сегодня равен {round(currency_dict[currency_name][0], 2)} руб. за {currency_dict[currency_name][1]}')
    else:
        print('Такой валюты не существует')


"""
AFTER MEMORY OPTIMIZATION
1. Выгрузка request в байтовую строку (размер объекта в 2 раза меньше)
2. Использование генератора и библиотеки recordclass вместо словаря
"""


def currency_get3():
    """function to get the list of names and values of all currencies for today"""
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').content
    print(f'размер сontent - {asizeof.asizeof((response))}')
    currency_rate = recordclass('currency_name', ('value', 'nominal'))
    for el in response.split(b'<CharCode>')[1:]:

        currency_name = str(el.split(b'</CharCode>')[0], 'UTF-8')
        value = str(((el.split(b'<Value>')[1]).split(b'</Value>')[0]).replace(b',', b'.'), 'UTF-8')
        nominal = int(el.split(b'<Nominal>')[1].split(b'</Nominal')[0])

        yield currency_rate(currency_name, (value, nominal))

@decor
def currency_rates3(currency_name):
    """ function to print the value of certain currency"""
    for el in currency_get3():

        if el.value == currency_name:
            print(f'Курс {currency_name} на сегодня равен {round(float(el.nominal[0]), 2)} руб. за {el.nominal[1]}')
            break


res, mem_diff = currency_rates2('USD')
res3, mem_diff3 = currency_rates3('USD')
print(f'Объем памяти ДО оптимизации - {mem_diff}')
print(f'Объем памяти ПОСЛЕ оптимизации - {mem_diff3}')
print(currency_rates('USD'))

