#Tic Tak Toe game with a little GUI.

import random

gme_board = [" 1 ", " 2 ", " 3 ",
             " 4 ", " 5 ", " 6 ",
             " 7 ", " 8 ", " 9 "]

def reset_board():
    global gme_board
    gme_board = [" 1 ", " 2 ", " 3 ",
                 " 4 ", " 5 ", " 6 ",
                 " 7 ", " 8 ", " 9 "]


#winner:
#        1,4,7 | 2,5,8 | 3,6,9 |
#        1,2,3 | 4,5,6 | 7,8,9 |
#        1,5,9 | 3,5,7 |

def is_winner(user_moves, comp_moves):
    winning_combo = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]

    ]

    for combo in winning_combo:
        if all(pos + 1 in user_moves for pos in combo):
            print("Whoo-hoo! You won.")
            return True
        elif all(pos + 1 in comp_moves for pos in combo):
            print("Whoo-hoo! Computer won.")
            return True
    return False


def game_board():

    print("          │        │       ")
    print(f"    {gme_board[0]}   │   {gme_board[1]}  │  {gme_board[2]}")
    print("          │        │       ")
    print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
    print("          │        │       ")
    print(f"    {gme_board[3]}   │   {gme_board[4]}  │  {gme_board[5]}")
    print("          │        │       ")
    print(" ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ")
    print("          │        │       ")
    print(f"    {gme_board[6]}   │   {gme_board[7]}  │  {gme_board[8]}")
    print("          │        │       ")
    print("\n")


def input_check(turn, left_choice): #For checking and validating the inputs of the user and the comp
    while True:
        if turn in left_choice:
            return True
        else:
            print("This place is already taken. Please choose another place: ")
            turn = int(input())


def logic(user_symbol, comp_symbol): #For logic
    left_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    user_moves = []
    comp_moves = []
    for i in range(1, 10):
        user_choice = int(input(f'Enter your choice from among the following choices: {left_choice}: '))
        print()
        if user_choice in left_choice:
            user_check = input_check(user_choice, left_choice)
            if user_check:
                gme_board[user_choice - 1] = user_symbol
                user_moves.append(user_choice)
                left_choice.remove(user_choice)
                if len(left_choice) != 0:
                    comp_choice = random.choice(left_choice)
                    comp_check = input_check(comp_choice, left_choice)
                    if comp_check:
                        gme_board[comp_choice - 1] = comp_symbol
                        comp_moves.append(comp_choice)
                        left_choice.remove(comp_choice)
                        print(f'Your choice is {user_choice}. \nComputer choice is {comp_choice}. ')
                        print()
                        game_board()
                        win = is_winner(user_moves, comp_moves)
                        if win:
                            print("Wanna play again? (Y/N)?")
                            play = input().upper()
                            if play == "Y":
                                reset_board()
                                user_symbol, comp_symbol = board()
                                logic(user_symbol, comp_symbol)
                                break
                            else:
                                print("Thank you for playing.")
                                break
                    else:
                        print("Computer choice is incorrect.")
                else:
                    print("All positions are already taken.")
                    print("\n")
                    break
        else:
            print("This place is already taken. Please choose another place: ")
            print("\n")


def board(): #For the initial printing of game design
    i = 1
    row = "          │        │       "
    col = " ━━━━━━━━━━━━━━━━━━━━━━━━━━━━ "

    name, user_symbol = user_input()
    if user_symbol == 'X':
        us = ' X '
        cs = ' O '
    else:
        us = ' O '
        cs = ' X '

    name = name[0].upper() + name[1:]

    print(f'{name} \t\t V/S \t\t Computer')
    print(f'    {us} \t\t\t\t\t {cs}')


    while i < 12:
        if i % 4 == 0:
            print(col)
        else:
            print(row)
        i += 1

    return us, cs

def user_input(): #For taking the symbol choice input from user
    while True:
        choice = input("Choose - (X/O): ").upper()
        if choice in ['X', 'O']:
            break
        else:
            print("Invalid choice! Please choose X or O.")
    name = input("Enter your name: ").lower()
    return name, choice


def main(): #For help menu and to continue to game
    while True:
        print(">>> Welcome to Tic-Tak! <<<")
        print("Commands: ")
        print("'H' -> for help in selecting positions.")
        print("'X' -> for exiting the game.")
        print("'C' -> to continue to game.")
        choice = input().upper()

        if choice == 'H':
            print(" 1 │ 2 │ 3  ")
            print("━━━━━━━━━━━━")
            print(" 4 │ 5 │ 6  ")
            print("━━━━━━━━━━━━")
            print(" 7 │ 8 │ 9  ")
            print("\n")
        elif choice == 'X':
            print("Thank you for playing.")
            break
        else:
            user_symbol, comp_symbol = board()
            logic(user_symbol, comp_symbol)


main()