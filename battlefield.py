import string
from field import Field

# The player's boards with ships on them
class PlayerField(Field):
    def __init__(self):
        super().__init__()
        self.initialize = self.set_up_ships()

# What the players choose from
class PlayerSelect(Field):
    def __init__(self):
        super().__init__()
