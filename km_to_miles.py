def is_convert(kilo):
    if kilo >= 0:
        print( kilo * .621371 )
    else:
        print("Kilometer is less than 0")
 
print("Enter the distance in kilometers: ")
kilo = float(input())

is_convert(kilo)