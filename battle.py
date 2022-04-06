from battlefield import PlayerField, PlayerSelect
import os

def clear():
    os.system('cls')

class Battle:
    def __init__(self):
        self.p1field = ""
        self.p2field = ""
        self.p1select = ""
        self.p2select = ""

    def run(self):
        self.greetings()
        self.game_setup()
        winner = self.turn_loop()
        self.win_announce(winner)

    def greetings(self):
        print("Welcome to Battleship!")
        input("Press enter to continue")

    def game_setup(self):
        print("First, player 1 please choose your ship locations")
        input("Press enter to continue")
        self.p1field = PlayerField()
        clear()
        print("Now that player 1 has set up their field, it is now time for player 2 to set up their field.")
        input("Player 2, press enter when you are ready to select where your ships will go on your field")
        self.p2field = PlayerField()
        clear()
        input("Now on to the game! Player 1 will go first. Press enter when ready.")
        self.p1select = PlayerSelect()
        self.p2select = PlayerSelect()

    def turn_loop(self):
        print('happening')
        turn = 1
        win_condition = 0
        while win_condition == 0:
            if turn == 2:
                self.p2_turn
                turn = 3
            if turn == 1:
                self.p1_turn
            if turn == 3:
                turn = 1
            if self.p1field.hp == 0:
                win_condition = 2
            if self.p2field.hp == 0:
                win_condition = 1
        return win_condition
  

    def p1_turn(self):
        clear()
        input("It's the next player's turn, please press enter when ready.")
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
        clear()
        input("It's the next player's turn, please press enter when ready.")
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

    def win_announce(self, winner):
        if winner == 1:
            print('Player 1 wins!')
        if winner == 2:
            print('Player 2 wins!')

    def print_field(self, playerfield):
        for each in playerfield.matrix:
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
