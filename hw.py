import random

class Game():
    def __init__(self):
        self.comp = random.randint(0, 5)
        print("Я загад число")
        self.your = int(input('введи число'))

    def gamme(self):
        if self.comp == self.your:
            print('Ты отгадал')
        else:
            print("неверно")

a = Game()
a.gamme()