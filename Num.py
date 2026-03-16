#This python code has the logic of various number types:
#Hululululu code :D

x = 1

def calc_fact(y):
    if y == 0 or y == 1:
        return 1
    return calc_fact(y - 1) * y

while x != 0:
    print()
    print('Enter "1" to access the code' )
    print('Enter "0" to exit the code' )
    print()

    x = int(input("Choice : "))

    if x == 1:
        print("Enter the choice as follows : ")
        print("1 -> Palindrome numb")
        print("2 -> Armstrong numb")
        print("3 -> Perfect numb")
        print("4 -> Automorphic numb")
        print("5 -> Harshad (Niven) numb")
        print("6 -> Spy numb")
        print("7 -> Neon numb")
        print("8 -> Strong numb")
        print("9 -> Duck numb")
        print("10 -> Buzz numb")


        c = int(input("Enter the numb code : "))

        n1 = input("Enter the number: ")
        n2 = int(n1)
        sq = n2 * n2
        f = False

        if c == 1:
            #1. Palindrome numb :
            rev = ""

            for i in n1:
                rev = i + rev

            if rev == n1:
                print("PALINDROME NUMB")
            else:
                print("NOT A PALINDROME NUMBER")

        elif c == 2:
            #2. Armstrong numb :
            total = 0
            i = 0
            while len(n1) > i :
                total = total + (int(n1[i]) ** len(n1))
                i += 1

            if total == n2:
                print("ARMSTRONG NUMB")
            else:
                print("NOT AN ARMSTRONG NUMB")

        elif c == 3:
            #3. Perfect numb :
            total = 0
            for i in range(1, n2):
                if n2 % i == 0:
                    total = total + i

            if total == n2:
                print("PERFECT NUMB")
            else:
                print("NOT A PERFECT NUMB")

        elif c == 4:
            #4. Automorphic numb :
            lst = sq % ( 10 ** len(n1))
            if n2 == lst:
                print("AUTOMORPHIC NUMB")
            else:
                print("NOT AN AUTOMORPHIC NUMB")

        elif c == 5:
            #5. Harshad (Niven) numb :
            total = 0
            for i in range(len(n1)):
                total = total + int(n1[i])

            if n2 % total == 0:
                print("HARSHAD (NIVEN) NUMB")
            else:
                print("NOT A HARSHAD (NIVEN) NUMB")

        elif c == 6:
            #6. Spy numb :
            total = 0
            prd = 1
            for i in range(len(n1)):
                total = total + int(n1[i])
                prd = prd * int(n1[i])

            if total == prd:
                print("SPY NUMB")
            else:
                print("NOT A SPY NUMB")

        elif c == 7:
            #7. Neon numb :
            total = 0
            for i in str(sq):
                total = total + int(i)

            if total == n2:
                print("NEON NUMB")
            else:
                print("NOT A NEON NUMB")

        elif c == 8:
            #8. Strong numb :
            total = 0
            for i in range(len(n1)):
                fct = calc_fact(int(n1[i]))
                total = total + fct

            if total == n2:
                print("STRONG NUMB")
            else:
                print("NOT A STRONG NUMB")

        elif c == 9:
            #9. Duck numb :
            if int(n1[0]) != 0:
                for i in range(1, len(n1)):
                    if n1[i] == 0:
                        f = True
                        break

            if f:
                print("DUCK NUMB")
            else:
                print("NOT A DUCK NUMB")

        elif c == 10:
            #10. Buzz numb :
            if int(n1[-1]) == 7 or n2 % 7 == 0:
                print("BUZZ NUMB")
            else:
                print("NOT A BUZZ NUM")

        else:
            print("END")
    else:
        print("EXITED")