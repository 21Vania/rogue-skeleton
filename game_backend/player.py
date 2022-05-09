

class Player:
    def __init__(self, symbol=u'\U0001F63C'):
        self._symbol = symbol
        self._x = None
        self._y = None

    def initPos(self, _map):
        n_row = len(_map)
        #n_col = len(_map[0])

        y_init = n_row//2
        found = False
        while found is False:
            y_init += 1
            for i,c in enumerate(_map[y_init]):
                if c == ".":
                    x_init = i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol

    def move(self, dx, dy, map):
        new_x = self._x + dx
        new_y = self._y + dy

# J'ai enlévé les croix que laisse le perso derrière lui qd il avance parce que cétait chiant
        if map[new_y][new_x] == ".": #or map[new_y][new_x] == "x" :
            ret =True
            map[new_y][new_x] = self._symbol
            #map[self._y][self._x] = "x"
            map[self._y][self._x] = "."
            #data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
        elif map[new_y][new_x] == u'\U0001F4B0' or map[new_y][new_x] == u'\U0001F9EA' or map[new_y][new_x] == u'\U0001F5E1':
            ret = True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
        else:
            ret = False
            data = []
        return data, ret