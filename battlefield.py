import string
from field import Field

# The player's boards with ships on them
class Player1_Field(Field):
    def __init__(self):
        super().__init__()
        self.initialize = self.set_up_ships()

class Player2_Field(Field):
    def __init__(self):
        super().__init__()
        self.initialize = self.set_up_ships()

# What the players choose from
class Player1_Select(Field):
    def __init__(self):
        super().__init__()

class Player2_Select(Field):
    def __init__(self):
        super().__init__()

