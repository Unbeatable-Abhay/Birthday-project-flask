tup = (1, 4, 9, 16, 25, 1, 39, 49, 64, 81, 100)
n = 0
i = int(input("Enter the number to be searched : "))

while n < len(tup) :
    if tup[n] == i:
        print("Found at : ", n)
    else:
        print("Not found")
    n += 1



