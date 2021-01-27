# class Student:
#     def __init__(self, name ,age):
#         self.name = name
#         self.age = age
#
#     def beka(self):
#         print(self.name, self.age)
#
# obj = Student('Beka', 21)
# obj.beka()


# ДЗ НУЖНО СОЗДАТЬ ИГРУ НАЙДИ ЦИФРУ КОМП ЗАГАДАЕТ ЧИСЛО ТЫ ДОЛЖЖЕН НАЙТИ С ПЕРВОЙ ПОПЫТКИ
# 



import random
class Game:
    list_of_choices = ['Камень', 'Ножницы', 'Бумага']
    def __init__(self):
        self.your_choices = int(input('Enter Number: [0,1,2]'))
        print('Yor choice is', self.list_of_choices[self.your_choices])
        self.comp_choices = random.randint(0,2)
        print('My choices is:', self.list_of_choices[self.comp_choices])

    def get_winner(self):
        if self.your_choices == self.comp_choices:
            print("Ничья")
        if self.your_choices == 0 and self.comp_choices == 1:
            print('Ты победил')
        if self.your_choices == 0 and self.comp_choices == 2:
            print('Ты проиграл')
        if self.your_choices == 2 and self.comp_choices == 1:
            print("you losse")
        if self.comp_choices == 0 and self.your_choices == 1:
            print('Ты проиграл')
        if self.comp_choices == 0 and self.your_choices == 2:
            print('Ты выйграл')



game = Game()
game.get_winner()