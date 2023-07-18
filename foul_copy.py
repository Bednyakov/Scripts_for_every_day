class Cell:
    title = 'Клетка'
    def __init__(self, index, busy=False):
        self.set_index(index)
        self.__busy = busy

    def set_index(self, index):
        if index in range(1, 10):
            self.__index = index
        else:
            raise Exception('Ошибка.')

    def get_busy(self):
        return self.__busy

    def get_index(self):
        return self.__index


class Player:
    title = 'Игрок'
    __num_player = 0
    def __init__(self):
        Player.__num_player += 1
        if Player.__num_player < 2:
            self.index = 'X'
        else:
            self.index = 'O'
    def get_numplayers(self):
        return Player.__num_player


p = Player
cell = Cell(9)
print(cell.get_busy())
print(cell.get_index())
print(p.get_numplayers)

