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

Это файл для второго скрипта

Курс Основы Python: урок 10 задание 2
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.


"""
from abc import ABC, abstractmethod
from memory_profiler import profile
from pympler import asizeof


#BEFORE OPTIMIZATION


class Cloth(ABC):
    expense_count = 0

    @abstractmethod
    def expense(self):
        pass


class Coat(Cloth):


    def __init__(self, v):
        self.v = v
        Coat.expense_count += self.expense


    def __str__(self):
        return f'Для пальто размером {self.v} требуется ткань в кол-ве {self.expense}, общий расход = {Coat.expense_count:.02f}'


    @property
    def expense(self):
        return float(self.v / 6.5 + 0.5)


class Suit(Cloth):

    def __init__(self, h):
        self.h = h
        Suit.expense_count += self.expense


    def __str__(self):
        return f'Для костюма размером {self.h} требуется ткань в кол-ве {self.expense}, общий расход = {Suit.expense_count:.02f}'


    @property
    def expense(self):
        return float(2 * self.h + 0.3)


"""
AFTER optimization
уменьшение занимаемой оперативной памяти
за счет slots в ООП
"""

class Coat2:

    expense_count = 0

    __slots__ = 'v'

    def __init__(self, v):
        self.v = v
        Coat2.expense_count += self.expense


    def __str__(self):
        return f'Для пальто размером {self.v} требуется ткань в кол-ве {self.expense}, общий расход = {Coat2.expense_count:.02f}'


    @property
    def expense(self):
        return float(self.v / 6.5 + 0.5)


class Suit2:

    expense_count = 0

    __slots__ = 'h'

    def __init__(self, h):
        self.h = h
        Suit2.expense_count += self.expense


    def __str__(self):
        return f'Для костюма размером {self.h} требуется ткань в кол-ве {self.expense}, общий расход = {Suit2.expense_count:.02f}'


    @property
    def expense(self):
        return float(2 * self.h + 0.3)


coat = Coat(48)
suit = Suit(1.8)

coat2 = Coat(56)
suit2 = Suit(1.6)

coat3 = Coat2(48)
suit3 = Suit2(1.8)

print(f'Память под coat - {asizeof.asizeof(coat)}')
print(f'Память под suit - {asizeof.asizeof(suit)}')
print(f'Память под coat2 - {asizeof.asizeof(coat2)}')
print(f'Память под suit2 - {asizeof.asizeof(suit2)}')
print(f'Память под coat3 (оптимиз.) - {asizeof.asizeof(coat3)}')
print(f'Память под suit3 (оптимиз.) - {asizeof.asizeof(suit3)}')
