import random 

def choices():
    com_choice = random.choice(['r', 'p', 's'])
    user_choice = input("What you say? 'r' for rock, 'p' for paper, 's' for scissors: ")

    return com_choice, user_choice

# win when - r > s, p > r, s > p
def is_winner():
    cc, uc = choices()

    if cc == uc:
        print("Ohh no, it's a tie.")
        print(f'You chose {uc}, while computer chose {cc}')
    elif uc == 'r' and cc == 's' or uc == 'p' and cc == 'r' or uc == 's' and cc == 'p':
        print("Whooo-hoo, You won!!!")
        print(f'You chose {uc}, while computer chose {cc}')
    else:
        print("Whoo-hoo, computer won!!!")
        print(f'You chose {uc}, while computer chose {cc}')

while True:
    print()
    print("Wanna play rock, paper, scissors? 🤔 (Y/N)?")
    print()
    ext = input().lower()
    if ext == 'y':
        is_winner()
    else:
        break


    
    