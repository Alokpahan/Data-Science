# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
# Equation of an area of a triangle is,area = (1/2)*base*height

def calculate_area(base, height):
    area = (1/2)*base*height
    return area


n1 = input("Enter the base: ")
n2 = input("Enter the height: ")
n1 = float(n1)
n2 = float(n2)
print("The area of a triangel is:", calculate_area(n1, n2))


print("\n")

# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area. Equation of rectangle's area is, rectangle_area=length*width
# If no shape is supplied then it should take triangle as a default shape


def calculate_area(d1, d2, shape):
    if shape == "triangle":
        area = (1/2) * d1 * d2
    else:
        area = d1 * d2
    return area


def tri():
    num1 = input("Enter the base: ")
    num2 = input("Enter the height: ")
    num1 = float(num1)
    num2 = float(num2)
    triangle_area = calculate_area(num1, num2, "triangle")
    print(f'The area of a triangle is: {triangle_area}')


def rec():
    num11 = input("Enter the length: ")
    num22 = input("Enter the width: ")
    num11 = float(num11)
    num22 = float(num22)
    rectangle_area = calculate_area(num11, num22, "rectangle")
    print(f'The area of a rectangle is: {rectangle_area}')


s = input("Select your choices: \n ('T' for triangle or 'R' for rectangle): ")
s = s.lower()  # Convert input to lowercase
if s == "t":
    tri()
elif s == "r":
    rec()
else:
    print("Error: Input shape is neither triangle nor rectangle.")


# Write a function called print_pattern that takes integer number as an argument and
# prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print,
# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(n):
    for i in range(n):
        s = ''
        for j in range(i):
            s = s+'*'
        print(s)


m1 = input("Enter a number to see your pattern: ")
m1 = int(m1)
print("Patter based on you input number of lines is equal to that number: ")
pattern = print_pattern(m1+1)
