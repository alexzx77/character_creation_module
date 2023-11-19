# import math
#
# # Спросим, что хорошего в этой библиотеке.
# print(print.__doc__)
#
# # Будет напечатано:
# # This module provides access to the mathematical functions
# # defined by the C standard.


# from math import sqrt
#
# message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
#           'квадратного корня из заданного числа'
# print(message)
#
#
# def calculate_square_root(Number: float):
#     """Вычисляет квадратный корень."""
#     return sqrt(Number)
#
#
# def calc(your_number):
#     """Проверяет на отрицательность."""
#     if your_number <= 0:
#         return
#     root = calculate_square_root(your_number)
#     print(
#         f'Мы вычислили квадратный корень из введённого вами числа.
#         Это будет: '
#         f'{root}')
#
#
# print(message)
# calc(25.5)

# from math import sqrt
#
# message = ('Добро пожаловать в самую лучшую программу для вычисления '
#            'квадратного корня из заданного числа')
#
#
# def calculate_square_root(number):
#     """Вычисляет квадратный корень
#     :param number:
#     :return:
#     """
#     return sqrt(number)
#
#
# def calc(your_number):
#     """Проверяет аргумент на положительное значение """
#     if your_number <= 0:
#         return
#
#     root = calculate_square_root(your_number)
#     print(f'Мы вычислили квадратный корень из введённого вами числа. '
#           f'Это будет: {root}')
#
#
# print(message)
# calc(25.5)

from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Логика атаки."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    """Логика защиты."""
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
    if char_class == 'healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} урона'


def special(char_name: str, char_class: str) -> str:
    """Применение специальных умений."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость '
                f'{80 + 25}»')
    if char_class == 'mage':
        return f'{char_name} применил специальное умение «Атака {5 + 40}»'

    if char_class == 'healer':
        return f'{char_name} применил специальное умение «Защита {10 + 30}»'


def start_training(char_name: str, char_class: str) -> str:
    """Аннотация к выбранному классу."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(
        'Введи одну из команд: attack — чтобы атаковать противника, defence '
        '— чтобы блокировать атаку противника или special — чтобы '
        'использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Логика выбора класса."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь играть: Воитель — '
            'warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print(
                'Воитель — дерзкий воин ближнего боя. Сильный, выносливый и '
                'отважный.')
        if char_class == 'mage':
            print(
                'Маг — находчивый воин дальнего боя. Обладает высоким '
                'интеллектом.')
        if char_class == 'healer':
            print(
                'Лекарь — могущественный заклинатель. Черпает силы из '
                'природы, веры и духов.')
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
            'чтобы выбрать другого персонажа ').lower()
    return char_class
