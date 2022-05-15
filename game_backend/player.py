import random

class Player:
    def __init__(self, symbol='@'): #u'\U0001F63C'
        self._symbol = symbol
        self._x = None
        self._y = None
        self.life = 1
        self.potion = 0
        self.weapon = 0
        self.money = 0

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
        #print(f"{map[new_y][new_x]=}")

        if self.life > 0:
            if map[new_y][new_x] == '.':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == 'l':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                self.life = self.life + 1
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == 'p':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                self.potion = self.potion + 1
                p = random.choice(["poison", "invicibility", "weapon"])
                if p == "poison":
                    self.life = self.life - 1
                elif p == "invicibility":
                    self.life = self.life + 1
                elif p == "weapon":
                    self.weapon = self.weapon + 1
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == 'w':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                self.weapon = self.weapon + 1
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == '$':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                self.money = self.money + 1
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == 'm':
                if self.weapon > 0:
                    ret = False
                    alive = True
                    monster_killed = True
                    self.weapon = self.weapon - 1
                    data = []
                    items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                else:
                    ret = False
                    alive = True
                    monster_killed = False
                    self.life = self.life - 1
                    data = []
                    items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                    if self.life == 0:
                        ret = False
                        alive = False
                        monster_killed = False
                        data = []
                        items = {"life": 0, "potion": self.potion, "weapon": self.weapon, "money": self.money}
            else:
                ret = False
                alive = True
                monster_killed = False
                data = []
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
        else:
            ret = False
            alive = False
            monster_killed = False
            data = []
            items = {"life": 0, "potion": self.potion, "weapon": self.weapon, "money": self.money}
        return data, ret, items, alive, monster_killed


class Player2:
    def __init__(self, symbol='%'): #symbol à modifier
        self._symbol = symbol 
        self._x = None
        self._y = None
        self.life = 1
        self.potion = 0
        self.weapon = 0
        self.money = 0

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
        #print(f"{map[new_y][new_x]=}")

        if self.life > 0:
            if map[new_y][new_x] == '.':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == 'l':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                self.life = self.life + 1
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == 'p':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                self.potion = self.potion + 1
                p = random.choice(["poison", "invicibility", "weapon"])
                if p == "poison":
                    self.life = self.life - 1
                elif p == "invicibility":
                    self.life = self.life + 1
                elif p == "weapon":
                    self.weapon = self.weapon + 1
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == 'w':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                self.weapon = self.weapon + 1
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == '$':
                ret = True
                alive = True
                monster_killed = False
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = "."
                self.money = self.money + 1
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":'.'}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                self._x = new_x
                self._y = new_y
            elif map[new_y][new_x] == 'm':
                if self.weapon > 0:
                    ret = False
                    alive = True
                    monster_killed = True
                    self.weapon = self.weapon - 1
                    data = []
                    items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                else:
                    ret = False
                    alive = True
                    monster_killed = False
                    self.life = self.life - 1
                    data = []
                    items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
                    if self.life == 0:
                        ret = False
                        alive = False
                        monster_killed = False
                        data = []
                        items = {"life": 0, "potion": self.potion, "weapon": self.weapon, "money": self.money}
            else:
                ret = False
                alive = True
                monster_killed = False
                data = []
                items = {"life": self.life, "potion": self.potion, "weapon": self.weapon, "money": self.money}
        else:
            ret = False
            alive = False
            monster_killed = False
            data = []
            items = {"life": 0, "potion": self.potion, "weapon": self.weapon, "money": self.money}
        return data, ret, items, alive, monster_killed

class Monster:
    def __init__(self, symbol='m'):
        self._symbol = symbol
        self._x = None
        self._y = None
        self.life = 1

    def initPos(self, _map):
        y_init = random.randint(1, len(_map) - 1)
        x_init = random.randint(1, len(_map[0]) - 1)
        while _map[y_init][x_init] == '#':
            y_init = random.randint(1, len(_map) - 1)
            x_init = random.randint(1, len(_map[0]) - 1)

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol

    def move(self, dx, dy, map):
        new_x = self._x + dx
        new_y = self._y + dy

        if map[new_y][new_x] == '.':
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