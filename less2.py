"""ИНКАПСУЛЯЦИЯ = скрытие данных """

# class BankAccount():
#     name = 'Bektur'  # Публичные даннные
#     __passport = 'AN 1221122'  #ИНКАПСУЛЯЦИЯ
#     _balance = 0  # Протектед защита кода от другого программиста
#
# a = BankAccount()
# print(a._balance, a.name,a.__passport)

"""ПОЛИМОРФИЗМ = это одинаковые функции работающие по разному"""

# class Cat:
#     def sing(self):
#         print('meaw')
#
# class Dog:
#     def sing(self):
#         print("gaf")
#
# chores = [Cat(), Dog(), Cat(), Dog(), Cat(), Dog()]
# for i in chores:
#     i.sing()

"""НАСЛЕДОВАНИЕ = это возможность наследовать свои функции"""

class Persen:
    def can_breathe(self):
        print('i can breathe')
    def can_kill(self):
        print('i can kill')

class Doctor(Persen):
    def heal(self):
        print('i can heal')

class Teacher(Doctor):
    def can_teach(self):
        print('i can teach')

t = Teacher()
t.can_breathe()