"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit

def revers(enter_num, revers_num=0):                    # 1.8451426000101492 sec
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):                  # 1.212643500068225  sec
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):                                    # 0.2724873999832198 sec
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    enter_num = str(enter_num)
    num_list = list(enter_num)
    num_list.reverse()
    return ''.join(num_list)


sample_num = 123456789
print(timeit('revers(sample_num)', globals=globals()))
print(timeit('revers_2(sample_num)', globals=globals()))
print(timeit('revers_3(sample_num)', globals=globals()))
# print(timeit('revers_4(sample_num)', globals=globals()))
# print(revers(sample_num))
# print(revers_2(sample_num))
# print(revers_3(sample_num))
# print(revers_4(sample_num))



# 2.0519890999421477
# 1.2917733999202028
# 0.2589262999827042
# 0.502830300014466


# revers - это рекурсия
# revers_2 - цикл
# revers_3 - переворот строки, строки Python  являются неизменяемыми последовательностями, поэтому
# срез [::-1] создает переверную копию строки и является самым быстрым алгоритмом!
# revers_4 - встроенная функция reverse для списка после преобразования числа в строку, а затем в список
# второй по эффективности алгоритм, но не очень лаконичный