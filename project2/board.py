"""
File: board.py
Author: Snigdha Darji
Date: 4/29/21
Section: 14
E-mail: sdarji1@umbc.edu
Description: has the board printing  for the battleship game
"""



class Board:

    #declares size, score, is_active boolean
    def __init__(self, size, score):
        """

        :param size: int, size of board
        :param score: int, keeps track of hits/miss
        """

        self.size = size
        #2D array for the game board
        self.game_board = [["  " for i in range(size)] for j in range(size)]
        self.is_active = True
        self.score = score



    #check if ship was hit by x,y
    #if repeated pos, then go again
    def register_shot(self, x, y):
        """

        :param x: int, x position for registering shot
        :param y: int, y position for registering shot
        :return: True/False
        """


        #MM = miss , HH= hit

        if self.game_board[y][x] == "MM" or self.game_board[y][x] == "HH":
            return False

        if self.game_board[y][x] != "  ":

            if self.game_board[y][x] == "Ca":
                print('You\'ve hit the Carrier!')
                self.game_board[y][x] = "HH"

            elif self.game_board[y][x] == "Ba":
                print('You\'ve hit the Battleship!')
                self.game_board[y][x] = "HH"

            elif self.game_board[y][x] == "Cr":
                print('You\'ve hit the Cruiser!')
                self.game_board[y][x] = "HH"

            elif self.game_board[y][x] == "Su":
                print('You\'ve hit the Submarine!')
                self.game_board[y][x] = "HH"


            elif self.game_board[y][x] == "De":
                print('You\'ve hit the Destroyer!')
                self.game_board[y][x] = "HH"




            self.score -= 1


        else:

            print('You missed')
            self.game_board[y][x] = "MM"

        return True



    #created another function to keep track of score for declaring winner at the end
    def get_score(self):
        """

        :return: int, score
        """
        return self.score



    #return the output of one of the grids
    # depending if it is active or not
    def get_board(self, active_board):
        """

        :param active_board: true/false, used for printing the board
        :return: variable board display, 2d lists of the completed board
        """

        #board_display variable for printing the spaces and lines for the gameboard
        board_display = ""

        #printing the board
        # print the first row

        for i in range(self.size):
            board_display += "  " + str(i)
        board_display += " \n"


        count = 0
        for row in self.game_board:

            board_display += str(count) + " "

            for col in row:
                # if active or not

                if not active_board and (col != "HH" or col != "MM"):
                    board_display += "  "

                else:
                    board_display += col
                board_display += "|"
            board_display += "\n"

            count += 1

        return board_display

    #places ship at start and end pos
    def place_ship(self, ship, pos, end_pos, ship_name):
        """

        :param ship: int, length of the ship
        :param pos: user input of (x,y) coordinates
        :param end_pos: string, user input of right (r) or down (d)
        :param ship_name: string, initials of the ship
        :return: True/False
        """

        y = pos[0]
        x = pos[1]

        for i in range(ship):

            #if user enters right
            if end_pos == 'r':

                #out of bounds or overlapping
                if y < 0 or y > (self.size - ship-1) or self.game_board[x][y+i] != "  ":
                    print("Invalid position or overlapping ships, try again.")
                    return False

            #if user enters down
            if end_pos == 'd':

                if x < 0 or x > (self.size - ship-1) or self.game_board[x+i][y] != "  ":
                    print("Invalid position or overlapping ships, try again.")
                    return False

        for j in range(ship):

            if end_pos == 'r':
                self.game_board[x][y+j] = ship_name
            if end_pos == 'd':
                self.game_board[x+j][y] = ship_name


        return True
