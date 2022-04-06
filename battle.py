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
        self.p1select = battlefield.PlayerSelect
        self.p2select = battlefield.PlayerSelect





    def p1_turn(self):
        print(clear)
        self.print_field(self.p1select)
        # Confirm player input is valid
        good = 0
        while good == 0:
            choice = "Player 1, choose where you would like to attack! Like (A20)"
            good = self.valid_choice(self,choice,self.p1select)
        # Verify if player input is a hit or miss
        hit_miss = self.check_arsenal(choice, self.p2field)
        if hit_miss == 1:
            for each in self.p1select.matrix:
                if choice in each:
                    each[each.index(choice)] = "++"
        if hit_miss == 0:
            print("Player 1 misses!")
            for each in self.p1select.matrix:
                if choice in each:
                    each[each.index(choice)] = "00"

    def p2_turn(self):
        print(clear)
        self.print_field(self.p2select)
        # Confirm player input is valid
        good = 0
        while good == 0:
            choice = "Player 2, choose where you would like to attack! Like (A20)"
            good = self.valid_choice(self,choice,self.p2select)
        # Verify if player input is a hit or miss
        hit_miss = self.check_arsenal(choice, self.p1field)
        if hit_miss == 1:
            for each in self.p2select.matrix:
                if choice in each:
                    each[each.index(choice)] = "++"
        if hit_miss == 0:
            print("Player 2 misses!")
            for each in self.p2select.matrix:
                if choice in each:
                    each[each.index(choice)] = "00"








    def print_field(self, playerfield):
        for each in self.playerfied.matrix:
            print(f'{each}')

    def valid_choice(self, choice, playerfield):
        for each in playerfield.matrix:
            if choice in each:
                return 1
            else:
                print("Please choose another option, that is invalid")
                return 0

    #checks to see if choice is in any of the point lists attributed to the ships, says hit or miss based on that
    def check_arsenal(self, choice, playerfield):
        one = self.check_destroyer(choice, playerfield)
        two = self.check_sub(choice, playerfield)
        three = self.check_bat1(choice, playerfield)
        four = self.check_bat2(choice, playerfield)
        five = self.check_air(choice, playerfield)
        total = one + two + three + four + five
        return total

    def check_destroyer(self, choice, playerfield):
        if choice in playerfield.destroyer.points:
            playerfield.destroyer.points.remove(choice)
            if playerfield.des_hp == 0:
                print('You sank their Destroyer!')
            else:
                print("You got a hit!")
            return 1
        else:
            return 0
        
    
    def check_sub(self, choice, playerfield):
        if choice in playerfield.submarine.points:
            playerfield.submarine.points.remove(choice)
            if playerfield.sub_hp == 0:
                print('You sank their Submarine!')
            else:
                print("You got a hit!")
            return 1
        else:
            return 0

    def check_bat1(self, choice, playerfield):
        if choice in playerfield.battleship_1.points:
            playerfield.battleship_1.points.remove(choice)
            if playerfield.bat1_hp == 0:
                print('You sank their Destroyer!')
            else:
                print("You got a hit!")
            return 1
        else:
            return 0

    def check_bat2(self, choice, playerfield):
        if choice in playerfield.battleship_2.points:
            playerfield.battleship_2.points.remove(choice)
            if playerfield.bat2_hp == 0:
                print('You sank their Destroyer!')
            else:
                print("You got a hit!")
            return 1
        else:
            return 0

    def check_air(self, choice, playerfield):
        if choice in playerfield.air_carrier.points:
            playerfield.air_carrier.points.remove(choice)
            if playerfield.air_hp == 0:
                print('You sank their Destroyer!')
            else:
                print("You got a hit!")
            return 1
        else:
            return 0
