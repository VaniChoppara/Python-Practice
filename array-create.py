#Python program for creating  arrays

import numpy as np

#Creating rank1 array
array1= np.array([1,2,3])
print("Array created with ranl1 \n",array1)
print(type(array1))
print(array1.dtype)

#Creating rank2 array
array2=np.array([[1,2],[3,4]])
print("Array created with rank2 \n",array2)
print(type(array2))

#creating array with tuple
array3=np.array((1,2,3))
print("Array created with tuple \n", array3)
print(type(array3))