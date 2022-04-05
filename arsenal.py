from ship import Ship

class Destroyer(Ship):
    def __init__(self):
        super().__init__(2, "Destroyer")
        
class Submarine(Ship):
    def __init__(self):
        super().__init__(3, "Submarine")

class Battleship_1(Ship):
    def __init__(self):
        super().__init__(4, "Battleship")

class Battleship_2(Ship):
    def __init__(self):
        super().__init__(4, "Battleship")

class Destroyer(Ship):
    def __init__(self):
        super().__init__(5, "Aircraft Carrier")