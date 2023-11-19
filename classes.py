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
        # напечатайте на экран вопрос в нужном формате
        print(f'{someone.name}, {question}')
        someone.answer_question(question)
        # запросите ответ на вопрос у someone

        print()  # этот print выводит разделительную пустую строку


class Mentor(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)


class CodeReviewer(Human):
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)


class Curator(Human):
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса

# объявите и реализуйте классы CodeReviewer и Mentor


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



# # импортируем функции из библиотеки math для рассчёта расстояния
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
#         super().__init__(latitude, longitude)
#         ...
#         self.name = name
#         self.population = population
#         # допишите код: сохраните свойства родителя
#         # и добавьте свойства name и population
#
#     def show(self):
#         print(f"Город {self.name}, население {self.population} чел.")
#
#
# class Mountain(Point):
#     def __init__(self, latitude, longitude, name, height):
#         super().__init__(latitude, longitude)
#         ...
#         self.name = name
#         self.height = height
#     # допишите код: напишите конструктор, в нём сохраните свойства родителя
#     # и добавьте свойства name и height
#
#     # Создайте метод show(self):
#     # информацию о горе нужно вывести в формате:
#     # "Высота горы <название> - <высота> м."
#     def show(self):
#         print(f"Высота горы {self.name} - {self.height} м.")
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
#     def repeat(self, phrase=' '):  # Добавьте метод repeat().
#         return f'Попугай {self.name} говорит: {phrase}'
#
#
# class Penguin(Bird):
#     def __init__(self, name, size, genus):
#         super().__init__(name, size)
#         self.genus = genus
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
#     def swimming(self):  # Добавьте метод swimming().
#         return f'Пингвин {self.name} плавает со средней скоростью 11 км/ч.'
#
#
# kesha = Parrot('Ара', 'средний', 'красный')
# kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')
#
#
# print(kesha.repeat('Кеша хороший!'))
# print(kowalski.swimming())

# Импортируйте datetime.
# import datetime as dt
# import time
#
# # Импортируйте time.
#
#
# class Quest:
#     def __init__(self, name, description, goal):
#         self.name = name
#         self.description = description
#         self.goal = goal
#         self.start_time = None
#         self.end_time = None
#         # Допишите два свойства класса.
#
#     # Напишите методы приема и сдачи квеста.
#     def accept_quest(self):
#         if self.start_time is not None:
#             return 'С этим испытанием вы уже справились.'
#         self.start_time = dt.datetime.now(tz=None)
#         return f'Начало "{self.name}" положено.'

#     def pass_quest(self):
#         if self.start_time is None:
#             return 'Нельзя завершить то, что не имеет начала!'
#         self.end_time = dt.datetime.now(tz=None)
#         completion_time = self.end_time - self.start_time
#         return (f'Квест "{self.name}" окончен. Время выполнения квеста: '
#                 f'{completion_time}')
#
#     def __str__(self):
#         if self.end_time is not None:
#             return f'Цель квеста {self.name} - {self.goal} Квест завершён.'
#         if self.start_time is not None and self.end_time is None:
#             return f'Цель квеста "{self.name}" - {self.goal} Квест выполняется.'
#         return f'Цель квеста "{self.name}" - {self.goal}'
#         # def __str__(self):
#         #     # Можно задать любую строку, например
#         #     # «Не печатай меня, ведь я — объект!».
#         #     # Но лучше пусть при печати выводится что-то осмысленное,
#         #     # например имя объекта и его основные параметры.
#         #     return (
#         #         f'Меч — «{self.name}». '
#         #         f'Выкован из материала {self.material}, '
#         #         f'длина клинка — {self.blade_length}, '
#         #         f'прочность — {self.strength}.'
#         #     )
#
# quest_name = 'Сбор пиксельники'
# quest_goal = 'Соберите 12 ягод пиксельники.'
# quest_description = '''
# В древнем лесу Кодоборье растёт ягода "пиксельника".
# Она нужна для приготовления целебных снадобий.
# Соберите 12 ягод пиксельники.'''
#
# new_quest = Quest(quest_name, quest_description, quest_goal)
#
# print(new_quest.pass_quest())
# print(new_quest.accept_quest())
# time.sleep(3)
# print(new_quest.pass_quest())
# print(new_quest.accept_quest())
# print(new_quest.__str__())


# import datetime as dt
# import time
#
#
# class Quest:
#     def __init__(self, name, description, goal):
#         self.name = name
#         self.description = description
#         self.goal = goal
#         self.start_time = None
#         self.end_time = None
#
#     def accept_quest(self):
#         if self.end_time:
#             return 'С этим испытанием вы уже справились.'
#         self.start_time = dt.datetime.now()
#         return f'Начало квеста "{self.name}" положено.'
#
#     def pass_quest(self):
#         if not self.start_time:
#             return 'Нельзя завершить то, что не имеет начала!'
#         self.end_time = dt.datetime.now()
#         completion_time = self.end_time - self.start_time
#         return (f'Квест "{self.name}" окончен.'
#                 f' Время выполнения квеста: {completion_time}')
#
#     def __str__(self):
#         if self.end_time:
#             return f'Цель квеста {self.name} - {self.goal} Квест завершён.'
#         elif self.start_time != None and self.end_time == None:
#             return f'Цель квеста {self.name} - {self.goal}. Квест выполняется.'
#         return f'Цель квеста {название_квеста} - {цель_квеста}. Квест выполняется.'
#
#     # Напишите код метода __str__.
#
#
# quest_name = 'Сбор пиксельники'
# quest_goal = 'Соберите 12 ягод пиксельники.'
# quest_description = '''
# В древнем лесу Кодоборье растёт ягода "пиксельника".
# Она нужна для приготовления целебных снадобий.
# Соберите 12 ягод пиксельники.'''
#
# new_quest = Quest(quest_name, quest_description, quest_goal)
#
# print(new_quest.pass_quest())
# print(new_quest.accept_quest())
# time.sleep(3)
# print(new_quest.pass_quest())
# print(new_quest.accept_quest())
#
# # Печатаем объекта класса Quest:
# print(new_quest)


# class Sword:
#
#     def __init__(self, name, blade_length, grip, material='сталь'):
#         self.name = name
#         self.blade_length = blade_length
#         self.material = material
#         self.grip = grip
#         self.strength = 100
#         print(f'Новый меч {name} выкован!')
#
#     def slashing_blow(self):
#         self.strength -= 10
#         return (f'Нанесён рубящий удар мечом {self.name}. '
#                 f'Радиус поражения: {self.blade_length}.')
#
#     def piercing_strike(self):
#         self.strength -= 5
#         return (f'Нанесён пронзающий удар мечом {self.name}. '
#                 f'Рукоять {self.grip} мягко легла в руку.')
#
#     def sharpen(self):
#         self.strength = 100
#         return (f'Меч "{self.name}" заточен,'
#                 f' {self.material} отлично поддалась обработке.')
#
#     # Вот он — новый метод! Именно в нём описывается то, что должно выводиться
#     # при печати объекта.
#     def __str__(self):
#         # Можно задать любую строку, например
#         # «Не печатай меня, ведь я — объект!».
#         # Но лучше пусть при печати выводится что-то осмысленное,
#         # например имя объекта и его основные параметры.
#         return (
#             f'Меч — «{self.name}». '
#             f'Выкован из материала {self.material}, '
#             f'длина клинка — {self.blade_length}, '
#             f'прочность — {self.strength}.'
#         )
#
#
# katana = Sword('Верный', 1.5,
#                'хват двумя руками')
# classic_sword = Sword('Дежурный', 1.2,
#                       'хват одной рукой')
#
# # Печатаем созданные объекты.
# print(katana)
# print(classic_sword)
