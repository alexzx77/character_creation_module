# from random import randint
#
#
# def attack(char_name, char_class):
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(-3, -1)}')
#
#
# def defence(char_name, char_class):
#     if char_class == 'warrior':
#         return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
#     if char_class == 'mage':
#         return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
#     if char_class == 'healer':
#         return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
#
#
# def special(char_name, char_class):
#     if char_class == 'warrior':
#         return (f'{char_name} применил специальное умение «Выносливость '
#                 f'{80 + 25}»')
#     if char_class == 'mage':
#         return (f'{char_name} применил специальное умение «Атака '
#                 f'{5 + 40}»')
#     if char_class == 'healer':
#         return (f'{char_name} применил специальное умение «Защита '
#                 f'{10 + 30}»')
#
#
# def start_training(char_name, char_class):
#     if char_class == 'warrior':
#         print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
#     if char_class == 'mage':
#         print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
#     if char_class == 'healer':
#         print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
#     print('Потренируйся управлять своими навыками.')
#     print('Введи одну из команд: attack — чтобы атаковать противника, '
#           'defence — чтобы блокировать атаку противника или '
#           'special — чтобы использовать свою суперсилу.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     cmd = ''
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd == 'attack':
#             print(attack(char_name, char_class))
#         if cmd == 'defence':
#             print(defence(char_name, char_class))
#         if cmd == 'special':
#             print(special(char_name, char_class))
#     return 'Тренировка окончена.'
#
#
# def choice_char_class():
#     approve_choice = None
#     char_class = None
#     while approve_choice != 'y':
#         char_class = input('Введи название персонажа, '
#                            'за которого хочешь играть: Воитель — warrior, '
#                            'Маг — mage, Лекарь — healer: ')
#         if char_class == 'warrior':
#             print('Воитель — дерзкий воин ближнего боя. '
#                   'Сильный, выносливый и отважный.')
#         if char_class == 'mage':
#             print('Маг — находчивый воин дальнего боя. '
#                   'Обладает высоким интеллектом.')
#         if char_class == 'healer':
#             print('Лекарь — могущественный заклинатель. '
#                   'Черпает силы из природы, веры и духов.')
#         approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
#                                'или любую другую кнопку, '
#                                'чтобы выбрать другого персонажа ').lower()
#     return char_class
#
#
# def main():
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class = choice_char_class()
#     print(start_training(char_name, char_class))
#
#
# main()


# def we_crash_all(name: str) -> str:
#     return 'Привет, ' + name + ', мы всё сломали!'
#
# print(we_crash_all(100))

# TEST_DATA: list[tuple[int, str, bool]] = [
#     (44, 'success', True),
#     (16, 'failure', True),
#     (4, 'success', False),
#     (21, 'failure', False),
# ]
#
# BONUS: float = 1.1
# ANTIBONUS: float = 0.8
#
#
# def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
#     current_rep += rep_points
#     if buf_effect:
#         return float(current_rep) * float(BONUS)
#     return current_rep
#
#
# def remove_rep(current_rep: float, rep_points: int, debuf_effect: bool) -> (
#         float):
#     current_rep -= rep_points
#     if debuf_effect:
#         return current_rep * ANTIBONUS
#     return current_rep
#
#
# def main(duel_res: list[tuple[int, str, bool]]) -> str:
#     current_rep: float = 0.0
#     for rep, result, effect in duel_res:
#         if result == 'success':
#             current_rep = add_rep(current_rep, rep, effect)
#         if result == 'failure':
#             current_rep = remove_rep(current_rep, rep, effect)
#     return (f'После {len(duel_res)} поединков, репутация персонажа — '
#             f'{current_rep:.3f} очков.')
#
#
# # Тестовый вызов функции main.
# print(main(TEST_DATA))


# Тестовые данные.
# TEST_DATA: list[tuple[int, str, bool]] = [
#     (44, 'success', True),
#     (16, 'failure', True),
#     (4, 'success', False),
#     (21, 'failure', False),
# ]
#
# BONUS: float = 1.1
# ANTIBONUS: float = 0.8
#
#
# def add_rep(current_rep: float, rep_points: int, buf_effect: bool):
#     current_rep += rep_points
#     if buf_effect:
#         return current_rep * BONUS
#     return current_rep
#
#
# def remove_rep(current_rep, rep_points, debuf_effect):
#     current_rep -= rep_points
#     if debuf_effect:
#         return current_rep * ANTIBONUS
#     return current_rep
#
#
# def main(duel_res):
#     current_rep: float = 0.0
#     for rep, result, effect in duel_res:
#         if result == 'success':
#             current_rep = add_rep(current_rep, rep, effect)
#         if result == 'failure':
#             current_rep = remove_rep(current_rep, rep, effect)
#     return (f'После {len(duel_res)} поединков, репутация персонажа — '
#             f'{current_rep:.3f} очков.')
#
#
# # Тестовый вызов функции main.
# print(main(TEST_DATA))


# from random import randint
#
# from graphic_arts.start_game_banner import run_screensaver
#
#
# def attack(char_name: str, char_class: str) -> str:
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(-3, -1)}')
#
#
# def defence(char_name: str, char_class: str) -> str:
#     if char_class == 'warrior':
#         return f'{char_name} блокировал {10 + randint(5, 10)} урона'
#     if char_class == 'mage':
#         return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
#     if char_class == 'healer':
#         return f'{char_name} блокировал {10 + randint(2, 5)} урона'
#
#
# def special(char_name: str, char_class: str) -> str:
#     if char_class == 'warrior':
#         return (f'{char_name} применил специальное умение «Выносливость '
#                 f'{80 + 25}»')
#     if char_class == 'mage':
#         return f'{char_name} применил специальное умение «Атака {5 + 40}»'
#
#     if char_class == 'healer':
#         return f'{char_name} применил специальное умение «Защита {10 + 30}»'
#
#
# def start_training(char_name: str, char_class: str) -> str:
#     if char_class == 'warrior':
#         print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
#     if char_class == 'mage':
#         print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
#     if char_class == 'healer':
#         print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
#     print('Потренируйся управлять своими навыками.')
#     print(
#         'Введи одну из команд: attack — чтобы атаковать противника, defence '
#         '— чтобы блокировать атаку противника или special — чтобы '
#         'использовать свою суперсилу.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     cmd: str = ''
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd == 'attack':
#             print(attack(char_name, char_class))
#         if cmd == 'defence':
#             print(defence(char_name, char_class))
#         if cmd == 'special':
#             print(special(char_name, char_class))
#     return 'Тренировка окончена.'
#
#
# def choice_char_class() -> str:
#     approve_choice: str = ''
#     char_class: str = ''
#     while approve_choice != 'y':
#         char_class = input(
#             'Введи название персонажа, за которого хочешь играть: Воитель — '
#             'warrior, Маг — mage, Лекарь — healer: ')
#         if char_class == 'warrior':
#             print(
#                 'Воитель — дерзкий воин ближнего боя. Сильный, выносливый и '
#                 'отважный.')
#         if char_class == 'mage':
#             print(
#                 'Маг — находчивый воин дальнего боя. Обладает высоким '
#                 'интеллектом.')
#         if char_class == 'healer':
#             print(
#                 'Лекарь — могущественный заклинатель. Черпает силы из '
#                 'природы, веры и духов.')
#         approve_choice = input(
#             'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
#             'чтобы выбрать другого персонажа ').lower()
#     return char_class
#
#
# if __name__ == '__main__':
#     run_screensaver()
#     print('Приветствую тебя, искатель приключений!')
#     print('Прежде чем начать игру...')
#     char_name: str = input('...назови себя: ')
#     print(f'Здравствуй, {char_name}! '
#           'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
#     print('Ты можешь выбрать один из трёх путей силы:')
#     print('Воитель, Маг, Лекарь')
#     char_class: str = choice_char_class()
#     print(start_training(char_name, char_class))
#

# from random import randint
#
#
# def attack(char_name: str, char_class: str) -> str:
#     """Логика атаки."""
#     if char_class == 'warrior':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(3, 5)}')
#     if char_class == 'mage':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(5, 10)}')
#     if char_class == 'healer':
#         return (f'{char_name} нанёс урон противнику равный '
#                 f'{5 + randint(-3, -1)}')
#
#
# def defence(char_name: str, char_class: str) -> str:
#     """Логика защиты."""
#     if char_class == 'warrior':
#         return f'{char_name} блокировал {10 + randint(5, 10)} урона'
#     if char_class == 'mage':
#         return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
#     if char_class == 'healer':
#         return f'{char_name} блокировал {10 + randint(2, 5)} урона'
#
#
# def special(char_name: str, char_class: str) -> str:
#     """Применение специальных умений."""
#     if char_class == 'warrior':
#         return (f'{char_name} применил специальное умение «Выносливость '
#                 f'{80 + 25}»')
#     if char_class == 'mage':
#         return f'{char_name} применил специальное умение «Атака {5 + 40}»'
#
#     if char_class == 'healer':
#         return f'{char_name} применил специальное умение «Защита {10 + 30}»'
#
#
# def start_training(char_name: str, char_class: str) -> str:
#     """Аннотация к выбранному классу."""
#     if char_class == 'warrior':
#         print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
#     if char_class == 'mage':
#         print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
#     if char_class == 'healer':
#         print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
#     print('Потренируйся управлять своими навыками.')
#     print(
#         'Введи одну из команд: attack — чтобы атаковать противника, defence '
#         '— чтобы блокировать атаку противника или special — чтобы '
#         'использовать свою суперсилу.')
#     print('Если не хочешь тренироваться, введи команду skip.')
#     cmd: str = ''
#     while cmd != 'skip':
#         cmd = input('Введи команду: ')
#         if cmd == 'attack':
#             print(attack(char_name, char_class))
#         if cmd == 'defence':
#             print(defence(char_name, char_class))
#         if cmd == 'special':
#             print(special(char_name, char_class))
#     return 'Тренировка окончена.'
#
#
# def choice_char_class() -> str:
#     """Логика выбора класса."""
#     approve_choice: str = ''
#     char_class: str = ''
#     while approve_choice != 'y':
#         char_class = input(
#             'Введи название персонажа, за которого хочешь играть: Воитель — '
#             'warrior, Маг — mage, Лекарь — healer: ')
#         if char_class == 'warrior':
#             print(
#                 'Воитель — дерзкий воин ближнего боя. Сильный, выносливый и '
#                 'отважный.')
#         if char_class == 'mage':
#             print(
#                 'Маг — находчивый воин дальнего боя. Обладает высоким '
#                 'интеллектом.')
#         if char_class == 'healer':
#             print(
#                 'Лекарь — могущественный заклинатель. Черпает силы из '
#                 'природы, веры и духов.')
#         approve_choice = input(
#             'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
#             'чтобы выбрать другого персонажа ').lower()
#     return char_class
#
# class Bird:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
#     def describe(self):
#         return f'Размер птицы {self.name} — {self.size}.'
#
#
# class Parrot(Bird):
#     def __init__(self, name, size, color):
#         super().__init__(name, size)
#         self.color = color
#
#
# class Penguin(Bird):
#     def __init__(self, name, size, genus):
#         super().__init__(name, size)
#         self.genus = genus
# kowalski = Penguin('Королевский','большой','Aptenodytes')
# kesha = Parrot('Ара', 'средний', 'красный')


#

# class Bird:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
#     def describe(self, full=False):
#         return f'Размер птицы {self.name} — {self.size}.'
#
#
# class Parrot(Bird):
#     def __init__(self, name, size, color):
#         super().__init__(name, size)
#         self.color = color
#
#     def repeat(self, phrase):
#         self.phrase = phrase
#         return f'Попугай {self.name} говорит: {self.phrase}.'
#
#     def describe(self, full=False):
#         if full:
#             return (f'Попугай {self.name} — заметная птица, '
#                     f'окрас её перьев — {self.color}, '
#                     f'а размер — {self.size}. '
#                     'Интересный факт: попугаи чувствуют ритм, '
#                     'а вовсе не бездумно двигаются под музыку. '
#                     'Если сменить композицию, '
#                     'то и темп движений птицы изменится.')
#         return super().describe()
#
#     # Добавьте метод repeat().
#
#
# class Penguin(Bird):
#     def __init__(self, name, size, genus):
#         super().__init__(name, size)
#         self.genus = genus
#
#     def swimming(self):
#         return f'Пингвин {self.name} плавает со средней скоростью 11 км/ч.'
#
#     def describe(self, full=False):
#         if full:
#             return (f'Размер пингвина {self.name} '
#                     f'из рода {self.genus} — {self.size}. '
#                     'Интересный факт: однажды группа геологов-разведчиков '
#                     'похитила пингвинье яйцо, '
#                     'и их принялась преследовать вся стая, '
#                     'не пытаясь, впрочем, при этом нападать. '
#                     'Посовещавшись, похитители вернули птицам яйцо, '
#                     'и те отстали. ')
#         return super().describe()
#
#     # Добавьте метод swimming().
#
#
# kesha = Parrot('Ара', 'средний', 'красный')
# kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')
#
# print(kesha.repeat('Кеша хороший!'))
# print(kowalski.swimming())

# импортируем функции из библиотеки math для рассчёта расстояния
# from math import radians, sin, cos, acos
#
#
# class Point:
#     def __init__(self, latitude, longitude):
#         self.latitude = radians(latitude)
#         self.longitude = radians(longitude)
#
#     # считаем расстояние между двумя точками в км
#     def distance(self, other):
#         cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
#         self.longitude - other.longitude)
#
#         return 6371 * acos(cos_d)
#
#
# class City(Point):
#     def __init__(self, latitude, longitude, name, population):
#         # допишите код: сохраните свойства родителя
#         # и добавьте свойства name и population
#
#     def show(self):
#         print(f"Город {self.name}, население {self.population} чел.")
#
#
# class Mountain(Point):
#     # допишите код: напишите конструктор, в нём сохраните свойства родителя
#     # и добавьте свойства name и height
#
#     # Создайте метод show(self):
#     # информацию о горе нужно вывести в формате:
#     # "Высота горы <название> - <высота> м."
#
#
# # эта функция печатает расстояние
# # между двумя любыми наследниками класса Point
# def print_how_far(geo_object_1, geo_object_2):
#     print(f'От точки «{geo_object_1.name}» до точки «{geo_object_2.name}» — {geo_object_1.distance(geo_object_2)} км.')
#
#
# # основной код
# moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
# everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
# chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)
#
# moscow.show()
# everest.show()
# print_how_far(moscow, everest)
# print_how_far(moscow, chelyabinsk)


class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
        # напечатайте на экран вопрос в нужном формате
        print(f'{someone.name}, {self.question}')
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)


# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')


print('\ndir() with no argument\n')
print(dir())
