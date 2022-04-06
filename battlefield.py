import string
from field import Field

# The player's boards with ships on them
class PlayerField(Field):
    def __init__(self):
        super().__init__()
        self.initialize = self.set_up_ships()
        self.des_hp = len(self.destroyer.points)
        self.sub_hp = len(self.submarine.points)
        self.bat1_hp = len(self.battleship_1.points)
        self.bat2_hp = len(self.battleship_2.points)
        self.air_hp = len(self.air_carrier.points)
        self.hp = self.des_hp + self.sub_hp + self.bat1_hp + self.bat2_hp + self.air_hp

# What the players choose from
class PlayerSelect(Field):
    def __init__(self):
        super().__init__()

