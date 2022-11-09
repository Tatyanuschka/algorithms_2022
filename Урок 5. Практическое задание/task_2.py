"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce
"""

from collections import defaultdict
from functools import reduce


def calculation_digits16():
    numbers = defaultdict(list)
    for i in range(2):
        num = input(f'Введите {i + 1}-ое 16-ричное число: ')
        num = list(num)
        numbers[int(''.join(num), 16)] = num
    # print(numbers)
    digit_sum = list(hex(sum(numbers.keys()))[2:].upper())
    digit_mul = list(hex(reduce(lambda x, y: x * y, numbers.keys()))[2:].upper())
    print(f'Сумма чисел равна: {digit_sum}')
    print(f'Произведение чисел равно: {digit_mul}')


calculation_digits16()

"""
2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""

class digits16:

    def __init__(self, num):
        self.num = int(num, 16)

    def __add__(self, other):
        return list(hex(self.num + other.num)[2:].upper())

    def __mul__(self, other):
        return list(hex(self.num * other.num)[2:].upper())

num1 = digits16(input('Введите первое 16-ричное число: '))
num2 = digits16(input('Введите второе 16-ричное число: '))
print(f'Сумма введенных чисел равна - {num1 + num2},\n'
      f'а их произведение - {num1 * num2}')