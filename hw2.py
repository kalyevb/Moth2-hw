"""Инкапсуляция 1 задание"""
class UserProf():
    __name = 'Bektur'
    __phone_number = '0055921231'
    __password =  'qwert1234'

s = UserProf
print(__name, __phone_number, __password)



"""Полиморфизм 2 задание"""
class Rectangle():
    def get_area(self):
        print('Площадь обьекта 500 кв2 метров')

class Circle():
    def get_area(self):
        print('Площадь 1000 кв2 метров')

class Square():
    def get_area(self):
        print('Площаль 100 кв2 метров')

Ploshad = [Square(), Circle(), Rectangle()]
for i in Ploshad:
    i.get_area()



"""Наследование 3 задание """
class Animal():
    def can_life(self):
        print("life")
    def can_kill(self):
        print('kill')
    def can_eat(self):
        print('eat')
class Cat(Animal):
    def can_sing(self):
        print("mia")
class Dog(Animal):
    def can_gaf(self):
        print('gaf')

a = Dog()
a.can_kill()