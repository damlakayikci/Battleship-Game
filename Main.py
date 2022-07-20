
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
# f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = False  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    n = 1

    bitir = True

    while bitir:  # we want this part to execute until the two players confirm placement

        my_list = []

        if n == 1:  # LIST COMPREHENSION
            tablo1_1 = [["-" for k in range(10)] for i in range(10)]
            tablo1_2 = [["-" for k in range(10)] for i in range(10)]
            my_list = [tablo1_1, tablo1_2]

        if n == 2:
            tablo2_1 = [["-" for k in range(10)] for i in range(10)]
            tablo2_2 = [["-" for k in range(10)] for i in range(10)]
            my_list = [tablo2_1, tablo2_2]

        print_3d_list(my_list)

        #            definitions
        dict_ship_names = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
        index_ships = {"carrier": 0, "battleship": 1, "cruiser": 2, "submarine": 3, "destroyer": 4}
        ship_names = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
        lowered_ship_names = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
        kalan_gemiler = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

        print_ships_to_be_placed()
        for x in ship_names:
            print_single_element(x)

        print_empty_line()
        print_player_turn_to_place(n)
        print_to_place_ships()

        t = True
        while t:

            dogru_input3 = ["h", "v"]

            while True:
                inp_ = input().strip()
                if inp_ == "":  # for code not to break if nothing is given
                    inp_ = "a "

                inp = inp_.split(" ")  # split the input an make a list

                while "" in inp:  # if innecessary spaces written, eliminate them
                    inp.remove("")

                istenen_gemi = inp[0]  # our first input is the name of the ship
                try:
                    istenen_gemi1 = istenen_gemi.lower()  # convert the ship name to a lowercase name
                except:  # if the input isn't composed of letters
                    print_incorrect_input_format()
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()

                    # to have the given ship name in sentencecase
                count = 0
                for mk in lowered_ship_names:
                    count += 1
                    if istenen_gemi1 == mk:
                        capitalized_gemi = ship_names[count - 1]
                        break

                try:  # for the code not to break when input isn't int
                    int(inp[1])
                except:
                    print_incorrect_input_format()
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                    continue
                try:  # for the code not to break when input isn't int
                    int(inp[2])
                except:
                    print_incorrect_input_format()
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                    continue

                if len(inp) < 4:  # for the code not to break when input doesn't have enough arguments
                    print_incorrect_input_format()
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                    continue

                satir_girdisi = int(inp[1]) - 1
                sutun_girdisi = int(inp[2]) - 1
                yon_girdisi = inp[3]
                if satir_girdisi > 9 or sutun_girdisi > 9 or satir_girdisi < 0 or sutun_girdisi < 0:  # for the code not to break when the coordinates aren't in board
                    print_incorrect_coordinates()
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                    continue
                elif istenen_gemi1 not in lowered_ship_names:  # for the code not to break when ship name is given wrong
                    print_incorrect_ship_name()
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                    continue

                if inp[3] not in dogru_input3:  # for the code not to break when orientation isn't right
                    print_incorrect_orientation()
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                    continue

                if capitalized_gemi not in kalan_gemiler:  # for the code not to break when given ship is already placed
                    print_ship_is_already_placed(capitalized_gemi)
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                else:
                    break

            if yon_girdisi == "h":  # this part is to place ships, when the player wants to place them horizontal
                damla = 0
                if satir_girdisi + dict_ship_names[istenen_gemi1] > 10:  # we first check if the ship fits in the board
                    print_ship_cannot_be_placed_outside(capitalized_gemi)
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                    continue
                for carpi in range(
                        dict_ship_names[istenen_gemi1]):  # then we check if all the coordinates are free to be placed
                    if my_list[n - 1][sutun_girdisi][satir_girdisi + carpi] == "-":
                        damla += 1
                for carpi in range(dict_ship_names[istenen_gemi1]):

                    if damla == dict_ship_names[istenen_gemi1]:
                        if my_list[n - 1][sutun_girdisi][satir_girdisi + carpi] == "-":
                            my_list[n - 1][sutun_girdisi][satir_girdisi + carpi] = "#"
                            if carpi == 0:
                                kalan_gemiler.remove(capitalized_gemi)
                    else:
                        print_ship_cannot_be_placed_occupied(capitalized_gemi)
                        break



            elif yon_girdisi == "v":  # this part is to place ships, when the player wants to place them vertical
                cagla = 0
                if sutun_girdisi + dict_ship_names[istenen_gemi1] > 10:  # we first check if the ship fits in the board
                    print_ship_cannot_be_placed_outside(capitalized_gemi)
                    print_3d_list(my_list)
                    print_ships_to_be_placed()
                    for x in kalan_gemiler:
                        print_single_element(x)
                    print_empty_line()
                    print_player_turn_to_place(n)
                    print_to_place_ships()
                    continue
                for carpi in range(
                        dict_ship_names[istenen_gemi1]):  # then we check if all the coordinates are free to be placed
                    if my_list[n - 1][sutun_girdisi + carpi][satir_girdisi] == "-":
                        cagla += 1
                for carpi in range(dict_ship_names[istenen_gemi1]):

                    if cagla == dict_ship_names[istenen_gemi1]:

                        if my_list[n - 1][sutun_girdisi + carpi][satir_girdisi] == "-":
                            my_list[n - 1][sutun_girdisi + carpi][satir_girdisi] = "#"
                            if carpi == 0:
                                kalan_gemiler.remove(capitalized_gemi)
                    else:
                        print_ship_cannot_be_placed_occupied(capitalized_gemi)
                        break

            print_3d_list(my_list)

            if len(kalan_gemiler) > 0:
                print_ships_to_be_placed()

                for kalan_gemi in kalan_gemiler:  # we print ships to be placed from the list
                    print_single_element(kalan_gemi)
                print_empty_line()
                print_player_turn_to_place(n)
                print_to_place_ships()

            if len(kalan_gemiler) == 0:  # if there is left no ship to be placed we move on to confirmation
                devam = True
                while devam:
                    kalan_gemiler = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                    print_confirm_placement()
                    confirmation = input().strip().lower()
                    if confirmation == "y":
                        t = False
                        devam = False
                        break
                    elif confirmation == "n":  # if confirmation is "n" we renew the table
                        my_list = []
                        if n == 1:
                            tablo1_1 = [["-" for k in range(10)] for i in range(10)]
                            tablo1_2 = [["-" for k in range(10)] for i in range(10)]
                            my_list = [tablo1_1, tablo1_2]

                        if n == 2:
                            tablo2_1 = [["-" for k in range(10)] for i in range(10)]
                            tablo2_2 = [["-" for k in range(10)] for i in range(10)]
                            my_list = [tablo2_1, tablo2_2]
                        print_3d_list(my_list)
                        print_ships_to_be_placed()
                        for x in ship_names:
                            print_single_element(x)

                        print_empty_line()
                        print_player_turn_to_place(n)
                        print_to_place_ships()
                        devam = False
                        break

                    else:
                        continue

                if confirmation == "n":
                    n = n
                if n == 2 and confirmation == "y":  # if second player confirms we move on to battle phase
                    bitir = False
                if n == 1 and confirmation == "y":  # if the first player confirms we move on to second player
                    n = n + 1

    count1 = 0
    count2 = 0
    n = 1
    son = True
    while son:
        # we keep count of hit ships to be able to terminate code
        if count1 == 17:
            son = False
            continue

        if count2 == 17:
            son = False
            continue

        if n == 1:
            my_list = [tablo1_1, tablo1_2]
        elif n == 2:
            my_list = [tablo2_1, tablo2_2]

        if n == 1:
            n_ = 2
        elif n == 2:
            n_ = 1

        print_3d_list(my_list)
        print_player_turn_to_strike(n)
        print_choose_target_coordinates()

        v = True
        while v:
            hedef = input().strip()
            target = hedef.split(" ")

            while "" in target:
                target.remove("")

            if len(target) < 2:  # the input must include at least 2 elements
                print_incorrect_input_format()
                print_3d_list(my_list)
                print_player_turn_to_strike(n)
                print_choose_target_coordinates()
                continue

            try:  # inputs mut be integers
                sutun_hedefi = int(target[0])
            except:
                print_incorrect_input_format()
                print_3d_list(my_list)
                print_player_turn_to_strike(n)
                print_choose_target_coordinates()
                continue
            try:
                satir_hedefi = int(target[1])
            except:
                print_incorrect_input_format()
                print_3d_list(my_list)
                print_player_turn_to_strike(n)
                print_choose_target_coordinates()
                continue

            if sutun_hedefi > 10:  # coordinates must be inside board
                print_incorrect_coordinates()
                print_3d_list(my_list)
                print_player_turn_to_strike(n)
                print_choose_target_coordinates()
                continue
            if satir_hedefi > 10:
                print_incorrect_coordinates()
                print_3d_list(my_list)
                print_player_turn_to_strike(n)
                print_choose_target_coordinates()
                continue
            else:
                break

        if n == 1:
            if my_list[1][satir_hedefi - 1][sutun_hedefi - 1] == "!":  # first check if the tile is already struck
                print_tile_already_struck()
                continue
            if my_list[1][satir_hedefi - 1][sutun_hedefi - 1] == "O":
                print_tile_already_struck()
                continue
            my_list = [tablo2_1, tablo2_2]  # print "!" if player hits
            if my_list[1][satir_hedefi - 1][sutun_hedefi - 1] == "#":
                print_hit()
                count1 += 1
                my_list[1][satir_hedefi - 1][sutun_hedefi - 1] = "!"
                my_list = [tablo1_1, tablo1_2]
                my_list[1][satir_hedefi - 1][sutun_hedefi - 1] = "!"
                continue
            elif my_list[1][satir_hedefi - 1][sutun_hedefi - 1] == "-":  # print "O" if player misses
                print_miss()
                my_list[1][satir_hedefi - 1][sutun_hedefi - 1] = "O"
                my_list = [tablo1_1, tablo1_2]
                my_list[1][satir_hedefi - 1][sutun_hedefi - 1] = "O"

                print_type_done_to_yield(n_)
                onayy = True
                while onayy:  # if player misses, we want confirmation to yield turn
                    onayAl = input().strip()
                    onay = onayAl.lower()
                    if onay != "done":
                        print_type_done_to_yield(n_)
                    else:
                        onayy = False
                n = 2





        elif n == 2:
            if my_list[0][satir_hedefi - 1][sutun_hedefi - 1] == "!":
                print_tile_already_struck()
                continue
            if my_list[0][satir_hedefi - 1][sutun_hedefi - 1] == "O":
                print_tile_already_struck()
                continue
            my_list = [tablo1_1, tablo1_2]
            if my_list[0][satir_hedefi - 1][sutun_hedefi - 1] == "#":
                print_hit()
                count2 += 1
                my_list[0][satir_hedefi - 1][sutun_hedefi - 1] = "!"
                my_list = [tablo2_1, tablo2_2]
                my_list[0][satir_hedefi - 1][sutun_hedefi - 1] = "!"
                continue

            elif my_list[0][satir_hedefi - 1][sutun_hedefi - 1] == "-":
                print_miss()
                my_list[0][satir_hedefi - 1][sutun_hedefi - 1] = "O"
                my_list = [tablo2_1, tablo2_2]
                my_list[0][satir_hedefi - 1][sutun_hedefi - 1] = "O"

                print_type_done_to_yield(n_)
                onayy = True
                while onayy:
                    onayAl = input().strip()
                    onay = onayAl.lower()
                    if onay != "done":
                        print_type_done_to_yield(n_)
                    else:
                        onayy = False
                n = 1

    if n == 1:
        my_list = [tablo1_1, tablo1_2]
    elif n == 2:
        my_list = [tablo2_1, tablo2_2]

    print_3d_list(my_list)

    print_player_won(n)

    print_thanks_for_playing()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

