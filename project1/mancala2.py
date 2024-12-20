"""
File:         mancala.py
Author:       Snigdha Darji
Date:         3/29/2021
Section:      14
E-mail:       sdarji1@umbc.edu
Description:  creating a modified version of Mancala
"""


BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '


def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
        draw_board is the function that you should call in order to draw the board.
    top_cups and bottom_cups are 2d lists of strings.
    Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
    mancala_a and mancala_b should be 2d lists of strings.
    Each string should be BLOCK_WIDTH in length, and each list should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6
    (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13
     (Each list should be at least BLOCK_HEIGHT in length, since each string in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length
     which represents the mancala at position 7.
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length
    which represents the mancala at position 0.

    """


    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP

    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
        Draw_mancala is a helper function for the draw_board function.
    :param fore_or_aft: front or back (0, or 1)
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
    :param the_board: a 2d-list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
        Draw block is a helper function for the draw_board function.
    :param the_board: the board is the 2d grid of characters we're filling in
    :param pos_x: which cup it is
    :param pos_y: upper or lower
    :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]


def get_player():
    """This function gets the players names
    :param: none
    :return: list of players
    ."""

    #if True:

    #gets the players names
    player_1 = input('Player 1 please tell me your name: ')
    player_2 = input('Player 2 please tell me your name: ')

    #returns list of players names
    return [player_1, player_2]
    

def take_turn(cups,stones_dict):
    """This function should print the board, ask for the new move,
    verify that it is a legal move, and then make it.
    There should be a way for you to signal from this function back to run_game
    that you have landed on a mancala and that player should get a new turn.

    :param cups: integer representing cup
    :return stones_dict: dictionary of cups and it's respective stones
    """


    #player 2 mancala @ index 0, player 1 @ index 7

   # stones_dict = { 0:0, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:0, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4 }
    stones_len = len(stones_dict)
    i = 0


    while cups in stones_dict:

        #since these are mancalas, the player would have to go again
        if cups == 0 or cups == 7:
            print('This is a mancala, not a valid move. Go again please...')

        else:

            #removes however many stones are in that spot
            stones_dict[cups] = stones_dict[cups] - stones_dict[cups]
            stones_dict[i % stones_len +1] = stones_dict[i % stones_len] + stones_dict[i % stones_len +1]

    #return stones_dict


def run_game():
    """This function should run the game, set up the board,
    alternate between players, and determine the winner at the end.
    You should create helper functions in order to distribute
    all of this functionality.
    :param: none
    :return: none
    """
    stones_dict = { 0: 0, 1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 0, 8: 4, 9: 4, 10: 4, 11: 4, 12: 4, 13: 4 }

    playing = True
    x = 0

    #starts the game by asking for players
    players = get_player()

    make_blocks(players,stones_dict)
    #draw_board(top_cups,bottom_cups,mancala_a,mancala_b)


    while playing:
        #alternates between players, this function returns the cup
        #player wants to move
        cup = alternate(x,players)

        #take_turn returns stones_dict after player makes a move
        take_turn(cup,stones_dict)
        make_blocks(players,stones_dict)

        winner(stones_dict,players)




def alternate(cup,players):

    """
    This function alternates between players and returns the chosen cup
    :param cup: an integer
    :param players: strings from get_player()
    :return: integer cup player wishes to move
    """

    turn = 0
    flag = True

    while flag:

        #if even, player 1 goes
        if turn % 2 == 0:
            cup = int(input('{} What cup do you want to move? '.format(players[0])))
            make_blocks(players)

        #if odd, player 1 goes
        elif turn % 2 == 1:
            cup = int(input('{} What cup do you want to move? '.format(players[1])))
            make_blocks(players)

        turn+=1



    return cup


def make_blocks(players,dict):
    """
    Helper function for draw board. Creates 2D lists for top/bottom
    cups. 1D list for mancala_a and mancala_b
    :param players: string, name of players
    :param dict: for number of stones
    :return: none
    """

    top_cups = []
    bottom_cups = []

    mancala_a = []
    mancala_b = []

    # height comes first because the x's are on the sides/vertical
    for j in range(BLOCK_HEIGHT):
        row = []

        # y is on top for width/horizontal
        # appends values by column
        for i in range(BLOCK_WIDTH):

            #fills in the words to set up board
            if i == 0:
                row.append('Cup      ')

            elif i == 2:
                row.append('Stones')

            else:
                row.append(' ')
        # appends to a list to create a 2d list
        top_cups.append(row)
        bottom_cups.append(row)


    for j in range(2 * BLOCK_HEIGHT + 1):

        if j == 3:
            #not sure why this wasn't printing the player
            #names on the board
            mancala_a.append(players[0])

            mancala_b.append(players[1])
        # appends to a list to create a 2d list

    draw_board(top_cups, bottom_cups, mancala_a, mancala_b)


def winner(stones_dict,players):

    """
    "checks if a "row" is empty, 0 stones and determines a winner"
    :param stones_dict: dictionary of cups and stones
    :param players: strings from get_players()
    :return: none
    """

    stones = 0
    count = 0

    #player 1's row
    for cup in range(1,6):

        if stones in stones_dict[cup]:
            count+=1

        #counter variable
        #if all 6 have 0 stones, player is the winner
        if count == 6:
            print('{} is the winner!'.format(players[0]))
            flag = False

        else:
            flag = True

    # player 2's row
    for cup in range(8,13):

        if stones in stones_dict[cup]:
            count+=1

        if count == 6:
            print('{} is the winner!'.format(players[1]))
            flag = False

        else:
            flag = True



if __name__ == "__main__":

    run_game()

