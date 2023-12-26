import random

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

PLAYER, COMPUTER = 'X', 'O'

def reset_board():
    for row in range(3):
        for column in range(3):
            board[row][column] = ' '
            column += 1
        row += 1

def check_free_spaces():
    free_spaces = 9
    for row in range(3):
        for column in range(3):
            if board[row][column] != ' ':
                free_spaces -= 1
            column += 1
        row += 1
    return free_spaces

def print_board():
    print(' ', board[0][0], ' | ', board[0][1], ' | ', board[0][2], ' ')
    print('\n --------------- \n')
    print(' ', board[1][0], ' | ', board[1][1], ' | ', board[1][2], ' ')
    print('\n --------------- \n')
    print(' ', board[2][0], ' | ', board[2][1], ' | ', board[2][2], ' ')

def player_move(computer_prev_move, player_prev_move):
    row = computer_prev_move[0]
    column = computer_prev_move[1]
    while row > 2 or column > 2 or board[row][column] != ' ':
        row = int(input("Enter the row:(1-3) "))
        row -= 1
        column = int(input("Enter the column:(1-3) "))
        column-= 1
        if board[row][column] == ' ':
            break
        print("Invalid move, enter again\n")
    board[row][column] = PLAYER
    player_prev_move[0] = row
    player_prev_move[1] = column

def computer_move():
    if check_free_spaces() > 0:
        row = random.randint(0,2)
        column = random.randint(0,2)
        while board[row][column] != ' ':
            row = random.randint(0,2)
            column = random.randint(0,2)
            if board[row][column] == ' ':
                break
        board[row][column] = COMPUTER
    else :
        pass

    '''
def computer_move(computer_prev_move, player_prev_move):
    row = computer_prev_move[0]
    column = computer_prev_move[1]
    if check_free_spaces() > 0:
        while row > 2 or column > 2 or board[row][column] != ' ':
            row = random.randint(0,2)
            column = random.randint(0,2)
            if check_free_spaces() == 9:
                row = random.choice([0,2])
                column = random.choice([0,2])
                #this is for testing purpose
                row = 2
                column = 0

            elif check_free_spaces() == 7:
                row = random.choice([0,2])
                column = random.choice([0,2])
                if player_prev_move == [1, 1]:
                    pass
                if player_prev_move[0] == computer_prev_move[0]:
                    if (player_prev_move[1] == computer_prev_move[1]+1 or
                        player_prev_move[1] == computer_prev_move[1]-1):
                        if computer_prev_move[0] == 2:
                            row = computer_prev_move[0]-2
                        else:
                            row = computer_prev_move[0]+2
                        column = computer_prev_move[1]
                if player_prev_move[1] == computer_prev_move[1]:
                    if (player_prev_move[0] == computer_prev_move[0]+1 or
                        player_prev_move[0] == computer_prev_move[0]-1):
                        if computer_prev_move[1] == 2:
                            column = computer_prev_move[1]-2
                        else:
                            column = computer_prev_move[1]+2
                        row = computer_prev_move[0]
            elif check_free_spaces() == 5:
                row = random.randint(0,2)
                if row == 1:
                    column = 1
                else:
                    column = random.choice([0,2])
            elif check_free_spaces() == 3:
                pass
            elif check_free_spaces() == 1:
                pass
            if board[row][column] == ' ':
                break
        board[row][column] = COMPUTER
        computer_prev_move[0] = row
        computer_prev_move[1] = column
    else:
        pass
    '''

def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][0] == board[row][2]:
            return board[row][0]
        row += 1
    for column in range(3):
        if board[0][column] == board[1][column] and board[0][column] == board[2][column]:
            return board[0][column]
        column += 1
    for index in range(3):
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return board[0][0]
        index += 1
    for index in range(3):
        if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            return board[0][2]
        index += 1
    return ' '

def print_winner(winner):
    if winner == PLAYER:
        print("You Won!")
    elif winner == COMPUTER:
        print("You Lose!")
    else:
        print("It's a tie")

def main():
    response = 'Y'
    while response == 'Y':
        winner = ' '
        reset_board()
        computer_prev_move = [4, 4]
        player_prev_move = [4, 4]
        while winner == ' ' and check_free_spaces() != 0:
            if winner != ' ' or check_free_spaces() == 0:
                break
            computer_move()
            #computer_move(computer_prev_move, player_prev_move)
            winner = check_winner()
            print_board()
            player_move(computer_prev_move, player_prev_move)
            winner = check_winner()
        print_board()
        print_winner(winner)
        response = input("Another Round? (Y/N)").upper()
    print("Thank You!")

main()
