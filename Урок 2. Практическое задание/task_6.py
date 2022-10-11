"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint


def num_guess(num, try_count=10):
    if try_count == 0:
        return print(f'Попытки закончились. Загаданное число - {num}')
    user_num = int(input(f'Угадайте число: '))
    if user_num > num:
        try_count -= 1
        print(f'Не угадали, загаданное число меньше. Осталось попыток - {try_count}!')
        return num_guess(num, try_count)
    elif user_num < num:
        try_count -= 1
        print(f'Не угадали, загаданное число больше. Осталось попыток - {try_count}!')
        return num_guess(num, try_count)
    else:
        return print('Вы угадали!!!')


num_guess(randint(0, 100))
