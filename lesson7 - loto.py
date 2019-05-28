import random

class Computer:

    def __init__(self, name):
        self.name = name

    def generate_card(self):
        card = []
        card_ = [' ', ' ']
        for i in range(3):
            card.append([random.randint(1, 90) for j in range(5)])
        print(*card_ + sorted(card[0]) + card_, sep = " ")
        print(*sorted(card[1]), sep = " ")
        print(*card_+ sorted(card[2]) + card_, sep = " ")
        return card


    def cross_out(self, card, B):
        inp = input('Зачеркнуть цифру? ' + str(B) + ' y/n ')
        inp = str(inp)
        text = 0
        for i, j in enumerate(card):
            if B in j and inp == 'y':
                card[i][j.index(B)] = '-'
                text = text + 1
            elif B in j and inp == 'n':
                text = text + 0
            elif (B not in j and inp == 'y'):
                text = text + 0
            elif (B not in j and inp == 'n'):
                text = text + 1
        if text >= 1:
            print('Игра продолжается')
            card_ = [' ', ' ']
            print(*card_ + card[0] + card_, sep=" ")
            print(*card[1], sep=" ")
            print(*card_ + card[2] + card_, sep=" ")
            return card
        elif text <= 0:
            print('Вы проиграли')
            card = []
            return card
        else:
            print('Вы ввели неверное значение. Введите y или n')


class Player(Computer):
    pass


newgamer1 = Computer('Компьютер')
print(newgamer1.name)
newgamer1 = Computer.generate_card(newgamer1)

newgamer2 = Player('Игрок')
print(newgamer2.name)
newgamer2_list = Player.generate_card(newgamer2)
newgamer2_cross_out = Player.cross_out(newgamer2, newgamer2_list, random.randint(1, 90))
while newgamer2_cross_out != []:
    newgamer2_cross_out = Player.cross_out(newgamer2, newgamer2_list, random.randint(1, 90))
    if newgamer2_cross_out == []:
        break
