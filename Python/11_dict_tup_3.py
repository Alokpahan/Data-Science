# Write circle_calc() function that takes radius of a circle as an input from user and 
# then it calculates and returns area, circumference and diameter. 
# You should get these values in your main program by calling circle_calc function and then print them


# Import the math module to access mathematical functions like pi
import math

# Function to calculate various properties of a circle based on its radius
def circle_cal(radius):
    # Calculate the area of the circle using the formula A = π * r^2
    area = math.pi * (radius ** 2)
    # Calculate the circumference of the circle using the formula C = 2 * π * r
    circumference = 2 * math.pi * radius
    # Calculate the diameter of the circle as 2 times the radius
    diameter = 2 * radius
    # Return the calculated values as a tuple (area, circumference, diameter)
    return area, circumference, diameter

# Main program logic
if __name__ == "__main__":
    # Prompt the user to input the radius of the circle
    r = input("Enter a radius:")
    r = float(r)  # Convert the input to a float
    # Call the circle_cal function to calculate area, circumference, and diameter
    area, cir, dia = circle_cal(r)
    # Print the calculated values
    print(f'Area: {area}, Circumference: {cir}, Diameter: {dia}')
