from . import battlefield

class Battle:
    def __init__(self):
        self.p1field = battlefield.Player1_Field()
        self.p1select = battlefield.Player1_Select()
        self.p2field = battlefield.Player2_Field()
        self.p2select = battlefield.Player2_Select()

