from sprites.enemy import Enemy


class BlueWinged(Enemy):
    def __init__(self, x, y, **kwargs):
        super().__init__(80, 48)