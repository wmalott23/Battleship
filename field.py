import string
from arsenal import AircraftCarrier, Battleship, Destroyer, Submarine

class Field:
    def __init__(self):
        self.alphabet = list(string.ascii_uppercase)
        self.matrix = self.create_field()
        self.destroyer = ""
        self.submarine = ""
        self.battleship_1 = ""
        self.battleship_2 = ""
        self.air_carrier = ""

    def create_field(self):
        field = []
        for each in range(0, 20):
            layer = []
            for each_two in range(0,20):
                layer.append(f"{self.alphabet[each]}{each_two+1}")
            field.append(layer)
        return field

    def print_field(self):
        for each in self.matrix:
            print(f'{each}')
    
    def place_ship(self, Ship):
        size = Ship.ship_size
        confirmation = 'n'
        # Find endpoints from User until they enter 'Y' for confirmation
        print(f"This ship is a {Ship.name} and takes up {size} points")
        while confirmation != 'y':
            option = self.place_first()
        # while loop repeats if middle points are over another ship
            rem_options = 'n'
            while rem_options == 'n':
                option_2 = self.place_endpoint(option, size)
                if size > 2:
                    rem_options = self.place_rest(option, option_2, size)
                if size < 3:
                    rem_options = ''
            confirmation = self.confirm_ship(option, option_2, rem_options, size)
        # Append points to ship, then reply with a confirmation print
        self.ship_append(option, option_2, rem_options, Ship)
        if size < 3:
            print(f'{Ship.name} has been placed at {option} and {option_2}')
        if size > 2:
            print(f'{Ship.name} has been placed at {option}, {rem_options}, {option_2}')
        

    def place_first(self):
        # Ask them for the initial input
        self.print_field()
        option = input(f'\nPick where you would like the starting point of your ship to go from the matrix above! Give a letter, then number (A20)\n')
        choice = 0
        # verify input is good, ask again if input is bad
        while choice != 1:
            for each in self.matrix:
                if option in each:
                    each[each.index(option)] = "+"
                    choice = 1
            if choice == 0:
                self.print_field()
                option = input(f'\n That is not a valid option, please enter one of the options seen above. Give a letter, then number (A20)\n')
        return option

    def place_endpoint(self, option, size):
        end_size = size - 1
        # Finding potential choices for user, checking if a letter above and below is on matrix, then checking if a number above and below is on the matrix
        pot_opt_1_letter = self.alphabet.index(option[0])-end_size
        pot_opt_2_letter = self.alphabet.index(option[0])+end_size
        pot_opt_1_alph = self.alphabet[pot_opt_1_letter]
        pot_opt_2_alph = self.alphabet[pot_opt_2_letter]
        pot_opt_3_number = int(option[1:])-end_size
        pot_opt_4_number = int(option[1:])+end_size
        pot_options = []
        if pot_opt_1_letter > -1 and pot_opt_1_letter < 20:
            pot_options.append(f'{pot_opt_1_alph}{option[1:]}')
        if pot_opt_2_letter > -1 and pot_opt_2_letter < 20:
            pot_options.append(f'{pot_opt_2_alph}{option[1:]}')
        if pot_opt_3_number > 0 and pot_opt_3_number < 21:
            pot_options.append(f'{option[0]}{pot_opt_3_number}')
        if pot_opt_4_number > 0 and pot_opt_4_number < 21:
            pot_options.append(f'{option[0]}{pot_opt_4_number}')
        print(pot_options)
        option_2 = input(f'\n Which endpoint would you like for the ship?\n')
        # Repeat question if user entry is not in pot_options, find the user option in the matrix if valid, change to + when found
        counter = 0
        while counter != 1:
            if option_2 in pot_options:
                for each in self.matrix:
                    if option_2 in each:
                        each[each.index(option_2)] = "+"
                        counter = 1
            if counter != 1:
                print(pot_options)
                option_2 = input(f'\n That is either an incorrect option or crosses over another ship. please select a different option. Try something like (A20)\n')
        return option_2


    def place_rest(self, option, option_2, size):
        # Finding the correct rate to increment
        opt_1_loc = self.alphabet.index(option[0])
        opt_2_loc = self.alphabet.index(option_2[0])
        alph_1 = int(option[1:])
        alph_2 = int(option_2[1:])
        alph_diff = opt_2_loc-opt_1_loc
        alph_inc = int(alph_diff / (size-1))
        num_diff = alph_2-alph_1
        num_inc = int(num_diff / (size-1))
        #Generating new points and appending them to a list and changing matrix with new point
        point_list = []
        for each in range(2,size):
            letter = self.alphabet[int(opt_1_loc + alph_inc)]
            number = alph_1 + num_inc
            point = (f'{letter}{number}')
            point_list.append(point)
            counter = 0
            for each in self.matrix:
                if point in each:
                    each[each.index(point)] = "+"
                    counter = 1
            if counter == 0:
                print("A middle point conflicts with another point, please choose again.\n")
                return 'n'
        return point_list

    def confirm_ship(self, option, option_2, rem_options, size):
        confirm = ''
        counter = 0
        while counter != 1:
            if size > 2:
                confirm = input(f'Does {option}, {rem_options}, {option_2} sound correct for this ship? (y/n)')
            if size < 3:
                confirm = input(f'Does {option}, {option_2} sound correct for this ship? (y/n)')
            if confirm == 'y' or confirm == 'n':
                counter = 1
            else:
                print('\nThat was not a valid entry, please enter (y/n)')
        return confirm


    def ship_append(self, option, option_2, rem_options, Ship):
        # append chosen points to ship.points
        Ship.points.append(option)
        Ship.points.append(option_2)
        for each in rem_options:
            Ship.points.append(each)        

    def set_up_ships(self):
        self.destroyer = Destroyer()
        self.submarine = Submarine()
        self.battleship_1 = Battleship()
        self.battleship_2 = Battleship()
        self.air_carrier = AircraftCarrier()
        self.place_ship(self.destroyer)
        self.place_ship(self.submarine)
        self.place_ship(self.battleship_1)
        self.place_ship(self.battleship_2)
        self.place_ship(self.air_carrier)