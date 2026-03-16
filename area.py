def is_area (a, b, c):
    area = a * b * c
    print(f"The area of the triangle is: {area} ")

print("Enter the sides of the triangle: ")
a = int(input())
b = int(input())
c = int(input())

is_area(a, b, c)