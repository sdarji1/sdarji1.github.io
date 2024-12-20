"""
File: battleship.py
Author: Snigdha Darji
Date: 4/29/21
Section: 14
E-mail: sdarji1@umbc.edu
Description: runs the battleship game
"""

from board import Board

# global constants
# dictionary of ship lengths
SHIPS = { "Ca" : 5, "Ba" : 4, "Cr" : 3, "Su" : 3, "De" : 2}

PLAYERS = ["p1", "p2"]



class BattleshipGame:

    # I can add any other helper functions
    def __init__(self, size=10):
        """

        :param size: size of the game board
        """

        #create the score tracker

        score = 0

        for ship in SHIPS:
            score += SHIPS[ship]

        self.playerOne_board = Board(size, score)  # create the player boards
        self.playerTwo_board = Board(size, score)
        self.size = size


    # ask to place ships
    # loop through turns

    def run_game(self):
        """

        :return: none
        """

        # starting the game

        print("Player 1, prepare to place your fleet.")
        self.place_ships(self.playerOne_board, PLAYERS[0])

        print("Player 2, prepare to place your fleet.")
        self.place_ships(self.playerTwo_board, PLAYERS[1])

        # going back and forth
        flag = True

        while (self.playerOne_board.get_score() != 0) and (self.playerTwo_board.get_score() != 0):
            #playerOne turn

            if self.playerTwo_board.get_score() != 0:

                self.display_boards(PLAYERS[0])

                x,y = input("Enter x y coordinates to fire: ").split()

                if self.playerTwo_board.register_shot(int(x),int(y)) == False:
                    print("You have already shot there, and hit/missed.")



            else:
                flag = False
                print('Congrats! Player 1 won!')


            #check winner after turn

            if self.playerOne_board.get_score() != 0:
                #playerTwo turn

                self.display_boards(PLAYERS[1])
                x,y = input("Enter x y coordinates to fire: ").split()


                if self.playerOne_board.register_shot(int(x),int(y)) == False:
                    print("You have already shot there, and hit/missed.")

            else:

                flag = False
                print('Congrats! Player 2 won!')





    # adds ships to the given board
    def place_ships(self, player_board,turn):
        """

        :param player_board: players board
        :param turn: list index of which players turn
        :return:
        """

        #prints active board when placing ships

        print(player_board.get_board(True))


        for ship in SHIPS:

            correct_pos = False
            while correct_pos == False:  # keep going until it fits

                x, y = input("Enter x y coordinates to place the " + ship + ": ").split()
                direction = input("Enter Right or Down (r or d): ")
                correct_pos = player_board.place_ship(SHIPS[ship], [int(x), int(y)], direction, ship)

            print(player_board.get_board(True))

            # depending on the turn, the current should see her
            # board clear and opponent board with hits/misses only

    def display_boards(self, turn):

        if turn == PLAYERS[0]:

            print("PLayer One Board: \n")
            print(self.playerOne_board.get_board(True))
            print("Player Two Board: \n")
            print(self.playerTwo_board.get_board(False))

        else:

            print("PLayer One Board: \n")
            print(self.playerOne_board.get_board(False))
            print("Player Two Board: \n")
            print(self.playerTwo_board.get_board(True))


if __name__ == '__main__':
    bs = BattleshipGame()
    bs.run_game()

