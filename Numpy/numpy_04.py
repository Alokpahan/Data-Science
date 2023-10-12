import numpy as np

# Slicing/stacking and indexing with boolean arrays

a = np.array([1,2,3,4,5,6,7,8])
print("Slicing operation by using +ve indexing:",a[0:3])
print("Slicing operation by using -ve indexing:",a[-4:-1])
print("print 3nd element ",a[3])
print("slices every other numbers elements from the end with step size 2\n",a[-1::-2])  

a1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[14,15,16,17]])
print("2 dimensional array: \n",a1)
print("print 3nd element from 2nd row:",a1[1,2])
print("Slicing Operation:\n",a1[1:3])
print("Slicing Operation:\n",a1[-3:-1])
print("Slicing Operation using the start, stop, and step parameters:\n",a1[1:3,3])  #[start:stop,column]
print("Slicing Operation using the start, stop, and step parameters:\n",a1[-3:-1,-1])  #[start:stop,column]
print("Slicing Operation using the start, stop, and step parameters:\n",a1[0,1:3])  #[row,start:stop]
print("Slicing Operation using the start, stop, and step parameters:\n",a1[0,-3:-1])  #[row,start:stop]
print("Slices every other numbers elements from the end with step size 2\n",a1[-1::-2])  
print("printing the 3rd and 4th column using slicing operation\n",a1[:,2:4])


# Iterating Arrays
print("\n")
print("# Iterating Arrays\n")

a2 = np.array([[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
for row in a2:      # Printing arrays using iterating through 'row' 
    print(row)
    
print("\n")

# for x in a2:      # Printing arrays using iterating through 'x'
#     print(x) 
# Get the shape of the array
rows, cols = a2.shape

# Iterate through rows and columns to print each element
for i in range(rows):
    for j in range(cols):
        print(f"a2[{i}][{j}] ==> {a2[i][j]}")
        
# .flat attribute is used to obtain a 1D view of a multi-dimensional array or matrix. 
print("\n")
print("1D view of a multi-dimensional array or matrix:\n")
for element in a2.flat:
    print(element)
    
# sticking together two array

s1=np.arange(6).reshape(3,2)
s2=np.arange(6,12).reshape(3,2)
print("\n",s1)    
print("\n",s2)    
print("Vertical stacking: \n",np.vstack((s1,s2)))
print("Horizontal stacking: \n",np.hstack((s1,s2)))