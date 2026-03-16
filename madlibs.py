import random

code_name = []
lan_name = []
game_name = []
is_found = True
rng = int(input("Enter the range: "))
while is_found: # for infinite questioning
    for i in range(0, rng): # for a particular number of inputs
        cdnm = input("Enter code names: ")
        code_name.append(cdnm)

        lnm = input("Enter language names: ")
        lan_name.append(lnm)

        gmnm = input("Enter game names: ")
        game_name.append(gmnm)

        print("Wanna exit?")
        ext = input(" 'Y' or 'N' ").lower()
        if ext == 'y':
            is_found = False
            break
        else:
            together_list = [code_name, lan_name, game_name]
            all_list = random.choice(together_list)
            print()
            print(f'Hlw bro, my name is {random.choice(all_list)}, i love to {random.choice(all_list)}, and currently i am learning {random.choice(all_list)}. \n I love to play {random.choice(all_list)} and i am an ex-{random.choice(all_list)} player.')
            print()

