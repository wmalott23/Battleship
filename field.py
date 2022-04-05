import string
from arsenal import Destroyer

class Field:
    def __init__(self):
        self.alphabet = list(string.ascii_uppercase)
        self.matrix = self.create_field()

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
        confirmation = 0
        while confirmation != 1:
            option = self.place_first()
            option_2 = self.place_second(option)
            size = Ship.ship_size
            if size > 2:
                confirm = self.place_remaining(option, option_2, size).capitalize
            if confirm == 'Y':
                confirmation = 1

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

    def place_second(self, option):
        # Finding potential choices for user, checking if a letter above and below is on matrix, then checking if a number above and below is on the matrix
        pot_opt_1_letter = self.alphabet.index(option[0])-1
        pot_opt_2_letter = self.alphabet.index(option[0])+1
        pot_opt_3_number = int(option[1:])-1
        pot_opt_4_number = int(option[1:])+1
        pot_options = []
        if pot_opt_1_letter > -1 and pot_opt_1_letter < 20:
            pot_options.append(f'{pot_opt_1_letter}{option[1:]}')
        if pot_opt_2_letter > -1 and pot_opt_2_letter < 20:
            pot_options.append(f'{pot_opt_2_letter}{option[1:]}')
        if pot_opt_3_number > 0 and pot_opt_3_number < 21:
            pot_options.append(f'{option[0]}{pot_opt_3_number}')
        if pot_opt_4_number > 0 and pot_opt_4_number < 21:
            pot_options.append(f'{option[0]}{pot_opt_4_number}')
        print(pot_options)
        option_2 = input(f'\n Which direction would you like the rest of the ship to head?\n')
        # Repeat question if user entry is not in pot_options, find the user option in the matrix if valid, change to + when found
        counter = 0
        while counter != 1:
            if option_2 in pot_options:
                for each in self.matrix:
                    if option_2 in each:
                        each[each.index(option_2)] = "+"
                        counter = 1
            else:
                print(pot_options)
                option_2 = input(f'\n That is not an option, please select from above. Try something like (A20)\n')
        
        
    def place_remaining(self, option, option_2, size):
        # Finding the pattern between option letter and option 2 letter to determine letters for reamining ship points
        opt_index = self.alphabet.index(option[0])
        opt_2_index = self.alphabet.index(option_2[0])
        opt_alph_rate = opt_2_index - opt_index
        # Finding the pattern between option number and option 2 number to determine numbers for remaining ship points
        opt_int = int(option[1:])
        opt_2_int = int(option_2[1:])
        opt_int_rate = opt_2_int - opt_int
        # Create remaining ship points based on letter and number rates, append to a list
        rem_ship_points = []
        new_point_alph = opt_2_index
        new_point_int = opt_2_int
        for each in range(1,size-2):
            new_point = (f"{self.alphabet.index(new_point_alph+opt_alph_rate)}{new_point_int+opt_int_rate}")
            rem_ship_points.append(new_point)
        for each in rem_ship_points:
            for each_2 in self.matrix:
                if each in each_2:
                    each_2[each_2.index(each)] = "+"
        print(rem_ship_points)
        return input(f'These are the remaining points, is this correct? (Y/N)')









asdf = Field()
asdf.place_ship(Destroyer)
asdf.print_field()