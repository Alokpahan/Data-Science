#  3 main benefits of numpy array over a python list,
# less memory 
# fast 
# convinient

import numpy as np
import time
import sys
 
l = range(1000)
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)
print(array.size*array.itemsize)

SIZE=10000000
l1= range(SIZE)
l2= range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# python list
start=time.time()
result=[(x+y) for x , y in zip(l1,l2)]
print("Python list took: ",(time.time()-start)*1000)

# numpy array
start=time.time()
result=a1+a2
print("Numpy took: ",(time.time()-start)*1000)

