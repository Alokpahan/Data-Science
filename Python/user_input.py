# Write a program that can find area of a triangle. 
# It should take base and height as an input from user and using that it should print an area of a triangle
base= input("Enter value for base:")
height= input("Enter values for height:")
area= (1/2)*float(base)*float(height)
print(area)


# Write a program that takes file name with extension as an input and 
# prints just the file name without extension (you can assume that file extensions are always 3 character long)

extension=input("Enter a file name with extension:")
print(f'File name without extension:{extension[:-4]}')

print(f'File name without extension:{extension[:len(extension)-4]}')
print("File name without extension:",extension[:len(extension)-4])