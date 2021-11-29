from math import trunc
import random


while True:
    symbol = input('X or O ? ').upper()
    if( (symbol == 'X') or (symbol == 'O')):
        break
    else:
        print('Invalid input. Try again')

board = [
        '-','-','-',
        '-','-','-',
        '-','-','-'
    ]

def round_printer(cont):
    print('\n####################')
    print(f'### Round {cont}###')
    print('####################\n')

def print_board(board):
    print('Current board:')
    print('=================================')
    print('-\t0\t1\t2')
    print(f'0\t{board[0]}\t{board[1]}\t{board[2]}')
    print(f'1\t{board[3]}\t{board[4]}\t{board[5]}')
    print(f'2\t{board[6]}\t{board[7]}\t{board[8]}')
    print('=================================')

def validation_input(choice):
    while True:
        try:
            option = int(input(f'What {choice}? '))
            if(option>=0 and option<3):
                return option
            else:
                print('Index not in range, only 0,1 or 2. Try again')
        except ValueError:
            print('Invalid input, only numbers')

def turn_player(option,board):
    print(f'Player {option} turn:')
    while True:
        while True:
            row=validation_input('row')
            column=validation_input('column')
            validation = input(f'Place {option} at row {row}, column {column} ? Y/N ').upper()
            if(validation=='Y'):
                break
        index = row*3 + column
        if(board[index]=='-'):
            board[index]=option
            print('Move placed!')
            print_board(board)
            break
        else:
            print('Box used. Invalid movement')

def turn_computer(option,board):
    print(f'Player {option} turn:')
    while True:
        index=random.randint(0,8)
        if(board[index]=='-'):
            board[index]=option
            print('Computer move registered ')
            print_board(board)
            break

def win_condition(option,board):
    win_condtions = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for line in win_condtions:
        win = True
        for w in line:
            if(board[w]!=option):
                win = False
        if(win):
            print(f'Player {option} wins!!')
            return True
    return False

def draw_condition(board):
    if(len([i for i in board if i=='-'])>0):
        return False
    print('IS A DRAW')
    return True

def game(board):
    cont=1
    round_printer(cont)
    print_board(board)
    computer_symbol = 'O' if symbol =='X' else 'X'
    while True:
        turn_player(symbol,board)
        win=win_condition(symbol,board)
        draw = draw_condition(board)
        if(win or draw):
            break
        turn_computer(computer_symbol,board)
        win=win_condition(computer_symbol,board)
        draw = draw_condition(board)
        if(win or draw):
            break

game(board)