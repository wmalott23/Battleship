from . import battlefield

clear = "\n"*50

class Battle:
    def __init__(self):
        self.p1field = ""
        self.p2field = ""
        self.p1select = ""
        self.p2select = ""

    def run(self):
        self.greetings(self)
        self.game_setup(self)






    def greetings(self):
        print("Welcome to Battleship!")

    def game_setup(self):
        print("First, player 1 please choose your ship locations")
        self.p1field = battlefield.PlayerField
        print({clear})
        print("Now that player 1 has set up their field, it is now time for player 2 to set up their field.")
        print("Player 2, please select where your ships will go on your field")
        self.p2field = battlefield.PlayerField
        print({clear})
        print("Now on to the game! Player 1 will go first.")

    
