import random
class Game():
    list_of_choices = ['1 door', '2 door', '3 door']

    def __init__(self):
        self.comp_choices = 1
        print('В одной из двери стоить авто:')
        self.your = int(input('Выбери дверь:'))
        print('ты выбрал', self.list_of_choices[self.your])

    def get_winner(self):
        if self.your == self.comp_choices:
            print("Я открою первую дверь", ' Ой тут нечего нет')
            go_first = int(input("Какую дверь теперь хочешь открыть (2/3): "))
            if go_first == 2:
                print("Ты выйграл АВТОМОБИЛЬ")
            else:
                print("Увы ты проиграл")
        if self.your == 0 and self.comp_choices == 1:
            print("Я открою третью дверь", ' Ой тут нечего нет')
            go_first = int(input("какую дверь теперь хочешь открыть (1/2): "))
            if go_first == 2:
                print("Ты выйграл АВТОМОБИЛЬ")
            else:
                print("Увы ты проиграл")
        if self.your == 2 and self.comp_choices == 1:
            print("Я открою первую дверь", ' Ой тут нечего нет')
            go_first = int(input("какую дверь теперь хочешь открыть (2/3): "))
            if go_first == 2:
                print("Ты выйграл АВТОМОБИЛЬ")
            else:
                print("Увы ты проиграл")

game = Game()
game.get_winner()