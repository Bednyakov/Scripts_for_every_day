class Cell:
    title = 'Клетка'
    def __init__(self, index, busy=False):
        self.index = index
        self.busy = busy

class Player:
    title = 'Игрок'
    num_player = 0
    def __init__(self):
        Player.num_player += 1
        if Player.num_player < 2:
            self.index = 'X'
        else:
            self.index = 'O'

class Board:
    title = 'Доска'
    def info(self):
        print(f'''
[{cell1.index}] [{cell2.index}] [{cell3.index}]
[{cell4.index}] [{cell5.index}] [{cell6.index}]
[{cell7.index}] [{cell8.index}] [{cell9.index}]''')


cell1 = Cell('1')
cell2 = Cell('2')
cell3 = Cell('3')
cell4 = Cell('4')
cell5 = Cell('5')
cell6 = Cell('6')
cell7 = Cell('7')
cell8 = Cell('8')
cell9 = Cell('9')
cellset = (cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9)

p1 = Player()
p2 = Player()
board1 = Board()
board1.info()

winline1 = (cell1, cell2, cell3)
winline2 = (cell4, cell5, cell6)
winline3 = (cell7, cell8, cell9)
winline4 = (cell1, cell5, cell9)
winline5 = (cell3, cell5, cell7)
winline6 = (cell1, cell4, cell7)
winline7 = (cell2, cell5, cell8)
winline8 = (cell3, cell6, cell9)
winset = (winline1, winline2, winline3, winline4, winline5, winline6, winline7, winline8)

def finish(winset):
    for set in winset:
        if set[0].busy == True and set[1].busy == True and set[2].busy == True:
            if set[0].index == set[1].index and set[0].index == set[2].index:
                print('Победа!')
                return False



start = True
while start:
    start = finish(winset)
    print(f'Игрок {p1.index}, ', end='')
    move_p1 = int(input('введите индекс клетки для хода: '))
    if cellset[move_p1 - 1].busy == False:
        cellset[move_p1 - 1].index = p1.index
        cellset[move_p1 - 1].busy = True
        print(board1.info())
    else:
        print('Пропуск хода...')

    start = finish(winset)
    print(f'Игрок {p2.index}, ', end='')
    move_p2 = int(input('введите индекс клетки для хода: '))
    if cellset[move_p2 - 1].busy == False:
        cellset[move_p2 - 1].index = p2.index
        cellset[move_p2 - 1].busy = True
        print(board1.info())
    else:
        print('Пропуск хода...')