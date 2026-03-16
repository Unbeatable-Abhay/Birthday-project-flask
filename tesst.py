tup = (1, 4, 9, 16, 1, 25, 39, 49, 64, 81, 100)
n = 0
i = int(input("Enter the number to be searched : "))
isFound = False
while n < len(tup) :
    if tup[n] == i:
        isFound = True
        break
    n = n + 1

if isFound:
    print("Value is found")
else:
    print("Valus is not found")