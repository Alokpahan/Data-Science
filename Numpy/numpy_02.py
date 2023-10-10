import numpy as np

# NumPy Creating Arrays and indexing

# 1 dimensional array
a = np.array([5, 6, 7])

# Display array type, number of dimensions, and the array itself
print("1-D array:")
print(type(a))
print("Dimensional of an array:",a.ndim)
print("Byte size of each element of an array",a.itemsize)    # byte size  as each element is integer type 
print(a)
print("The size of an array: ",a.size) # printing the total no of size of an array
# shape property
print("The information on dimensions(like width and height): ",a.shape)

b = np.array([50, 60, 70],dtype=np.float64)                  # consider the another array to convert it into 8 bytesa
print("Byte size of each element of an array",b.itemsize)     
print(b)
print("The size of an array: ",b.size) # printing the total no of size of an array
# shape property
print("The information on dimensions(like width and height): ",b.shape)

print("Printing using positive indexing:")
print(a[0])
print(a[1])
print(a[2])

# Negative indexing
print("Printing using negative indexing:")
print(a[-1])
print(a[-2])
print(a[-3])

# 2 dimensional array
b1 = np.array([[1, 2]])

# Display array type, number of dimensions, and the array itself
print("\n2-D array b1:")
print(type(b1))
print(b1.ndim)
print(b1)

print("Printing using positive indexing:")
print(b1[0, 0])
print(b1[0, 1])

print("Printing using negative indexing:")
print(b1[-1, -1])
print(b1[-1, -2])

b2 = np.array([[1, 2, 9], [3, 4, 7], [5, 6, 8]])

print("\n2-D array b2:")
print("Printing using positive indexing:")
print(b2)
print("The information on dimensions(like width and height): ",b2.shape)
print(b2[0, 0])
print(b2[0, 1])
print(b2[0, 2])
print(b2[1, 0])
print(b2[1, 1])
print(b2[1, 2])
print(b2[2, 0])
print(b2[2, 1])
print(b2[2, 2])

print("Printing using negative indexing:")
print(b2[-1, -1])
print(b2[-1, -2])

b3 = np.array([[1, 2, 9, 0, 3], [3, 4, 7, 56, 90]])

# Display array type and the array itself
print("\n2-D array b3:")
print(type(b3))
print(b3)

print("Printing by using positive indexing:")
print("5th element on 2nd row:", b3[1, 4])
print("5th element on 1st row:", b3[0, 4])
print("3rd element on 2nd row:", b3[1, 2])
print("3rd element on 1st row:", b3[0, 2])

print("Printing by using negative indexing:")
print("5th element on 2nd row:", b3[-1, -1])
print("5th element on 1st row:", b3[-2, -1])
print("3rd element on 2nd row:", b3[-1, -3])
print("3rd element on 1st row:", b3[-2, -3])

# 3 dimensional array
c = np.array([[[1, 2, 0], [3, 4, 1]], [[5, 6, 2], [7, 8, 3]], [[5, 6, 2], [7, 8, 3]]])

# Display array type and the array itself
c1 = np.array([[[11], [12], [13]]])
print("\n3-D array c1:")
print(type(c1))
print(c1)

print("Printing using positive indexing:")
print(c1[0, 0, 0])
print(c1[0, 1, 0])
print(c1[0, 2, 0])

print("Printing using negative indexing:")
print(c1[0, -1, 0])
print(c1[0, -2, 0])
print(c1[0, -3, 0])

c2 = np.array([[[11, 12], [13, 14], [15, 16]], [[21, 22], [23, 24], [25, 26]]])

# Display array type, number of dimensions, and the array itself
print("\n3-D array c2:")
print(type(c2))
print(c2.ndim)
print(c2)

print("Printing using positive indexing:")
print(c2[0, 0, 0])
print(c2[0, 0, 1])
print(c2[0, 1, 0])
print(c2[0, 1, 1])
print(c2[0, 2, 0])
print(c2[0, 2, 1])

print(c2[1, 0, 0])
print(c2[1, 0, 1])
print(c2[1, 1, 0])
print(c2[1, 1, 1])
print(c2[1, 2, 0])
print(c2[1, 2, 1])

print("Printing using negative indexing:")
print(c2[-1, -3, -2])
print(c2[-1, -3, -1])
print(c2[-1, -2, -2])
print(c2[-1, -2, -1])
print(c2[-1, -1, -2])
print(c2[-1, -1, -1])

print(c2[-2, -3, -2])
print(c2[-2, -3, -1])
print(c2[-2, -2, -2])
print(c2[-2, -2, -1])
print(c2[-2, -1, -2])
print(c2[-2, -1, -1])
