import numpy as np

# Basic array operation

# Initialization of an array with complex numbers:
a = np.array([[12,13,14],[15,16,17],[18,19,20]], dtype=complex)
print("Array with Complex numbers: \n",a)

# Zero() function
# Initialization of an array with placeholder numbers
print("Zero array: \n", np.zeros((3,4)))   # Initialization of array with all zeros
print("One array: \n", np.ones((3,4)))   # Initialization of array with all ones

# Range() function --> create a list
my_list = range(0,4)
print("List of numbers from 0 - 4(n-1):")
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

# arange() function --> create an array
arr = np.arange(0, 5) 
print("Array of 0 to 4:", arr)
arr1 = np.arange(0, 5, 2)       # Array from 0 to 4 with a step of 2
print("Array of 0 to 4 with a step of 2:", arr1)

# linspace() function
arr1 = np.linspace(1, 5, 10)  # Generate 10 numbers between 1 and 5 with linear spacing.
print(arr1)

arr2 = np.linspace(4, 10, 20)  # Generate 20 numbers between 4 and 10 with linear spacing.
print(arr2)

# Reshape() function
arr3 = np.array([[12,13,14,4],[15,16,17,7],[18,19,20,2]])
print("Original array: \n", arr3)
print("The shape of the original array: ", arr3.shape)
updated_shape = arr3.reshape(4, 3)
print("Reshaped array: \n", updated_shape)        
print("The shape of the reshaped array: ", updated_shape.shape)
updated_shape1 = arr3.reshape(12, 1)
print("Reshaped array: \n", updated_shape1)        
print("The shape of the reshaped array: ", updated_shape1.shape)

# Ravel() function
arr3 = np.array([[12,13,14,4],[15,16,17,7],[18,19,20,2]])
print("Original array: \n", arr3)
print("The shape of the original array: ", arr3.shape)
print("Raveled array: \n", arr3.ravel())

# Mathematical function

a1 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Original array: \n", a1)
print("Minimum value in the array: ", a1.min())
print("Maximum value in the array: ", a1.max())
print("Sum of all elements of the array: ", a1.sum())
print("Sum of all column elements of the array: ", a1.sum(axis=0))
print("Sum of all row elements of the array: ", a1.sum(axis=1))
print("Square root of each element of the array: ", np.sqrt(a1))
print("Standard Deviation of all elements of the array: ", np.std(a1))

# Mathematical operations

b1 = np.array([[1, 2, 9], [3, 4, 7], [5, 6, 8]])
b2 = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print("Addition of two arrays: \n", b1 + b2)
print("Subtraction of two arrays: \n", b2 - b1)
print("Multiplication of two arrays: \n", b1 * b2)
print("Division of two arrays: \n", b2 / b1)
print("Squaring each element of an array using ** operator: \n", b1 ** 2)
print("Squaring each element of an array using power() function: \n", np.power(b1, 2))

# Matrix operations

print("Matrix product of two matrices: \n", b1.dot(b2))  # Calculates matrix product using dot() function
print("Matrix product of two matrices: \n", np.dot(b1, b2))  # Calculates matrix product using dot() function
print("Transpose of a matrix: \n", b1.transpose())  # Calculates transpose using transpose() function
print("Transpose of a matrix: \n", np.transpose(b1))  # Calculates transpose using transpose() function
print("Inverse of a matrix: \n", np.linalg.inv(b1))  # Calculates inverse using linalg.inv() function
print("Determinant of a matrix: \n", np.linalg.det(b1))  # Calculates the determinant using linalg.det() function

# Flattening a matrix simply means converting a matrix into a 1D array.
print("Flatten of a matrix: \n", b1.flatten())  # Transforms a matrix into a 1D array using flatten() function
print("Flatten of a matrix: \n", np.ravel(b1))  # Transforms a matrix into a 1D array using ravel() function
print("Flatten of a matrix: \n", b1.ravel())  # Transforms a matrix into a 1D array using ravel() function
