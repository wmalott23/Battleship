from . import battlefield

class Battle:
    def __init__(self):
        self.p1field = battlefield.PlayerField()
        self.p2field = battlefield.PlayerField()
        self.p1select = battlefield.PlayerSelect()
        self.p2select = battlefield.PlayerSelect()