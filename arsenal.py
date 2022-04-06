from ship import Ship

class Destroyer(Ship):

    def __init__(self):
        super().__init__(2, "Destroyer")
        
class Submarine(Ship):
    def __init__(self):
        super().__init__(3, "Submarine")

class Battleship(Ship):
    def __init__(self):
        super().__init__(4, "Battleship")

class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__(5, "Aircraft Carrier")
