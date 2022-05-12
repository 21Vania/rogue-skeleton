

class Player:
    def __init__(self, symbol='@'): #u'\U0001F63C'
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
                if c == '.':
                    x_init = i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol

    def move(self, dx, dy, map):
        new_x = self._x + dx
        new_y = self._y + dy
        print("testing move function")
        print(f"{map[new_y][new_x]=}")

# J'ai enlévé les croix que laisse le perso derrière lui qd il avance parce que cétait chiant
        if map[new_y][new_x] == '.': #or map[new_y][new_x] == "x" :
            ret = True
            map[new_y][new_x] = self._symbol
            #map[self._y][self._x] = "x"
            map[self._y][self._x] = "."
            #data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
        elif map[new_y][new_x] == 'p' or map[new_y][new_x] == 'w' or map[new_y][new_x] == 'l' or map[new_y][new_x] == 'm':
            ret = True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
        else:
            ret = False
            data = []
        return data, ret


class Player2:
    def __init__(self, symbol='%'): #symbol à modifier
        self._symbol = symbol 
        self._x = None
        self._y = None

    def initPos(self, _map):
        n_row = len(_map)
        n_col = len(_map[0])

        y_init = n_row//2
        found = False
        while found is False:
            y_init += 1
            for i,c in reversed(list(enumerate(_map[y_init]))): #on doit parcourir la liste à l'envers
                if c == ".":
                    x_init = i     #on le place initialement à l'opposé du premier jour, tout à droite vers le milieu du coté
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
            print("first condition reached")
            ret = True
            map[new_y][new_x] = self._symbol
            #map[self._y][self._x] = "x"
            map[self._y][self._x] = "."
            #data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
        elif map[new_y][new_x] == 'p' or map[new_y][new_x] == 'w' or map[new_y][new_x] == 'l' or map[new_y][new_x] == 'm':
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