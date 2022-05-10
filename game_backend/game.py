from .map_generator import Generator
from .player import Player
from .player import Player2


class Game:
    def __init__(self, width=96, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level

        self._player = Player()
        self._player.initPos( self._map )

        self._player2 = Player2()
        self._player2.initPos( self._map )

    def getMap(self):
        return self._map

    def move(self, dx, dy):
        return self._player.move(dx, dy, self._map)

    def move2(self, dx, dy):
        return self._player2.move(dx, dy, self._map)