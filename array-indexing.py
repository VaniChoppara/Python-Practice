#Python progaram to demonstarte indexing an array
import numpy as np

#Initial array
arr= np.array([
    [-1,2,0,4],
    [4,-0.5,6,0],
    [2.6,0,7,8],
    [3,-7,4,2.0]
])
#printing Initial array
print("Initial arra:\n",arr)
print(arr.dtype)

#printing range of array using slicing
sliced_arr=arr[:2,::3];
print("Array with 2 rows and alternate columns \n", sliced_arr)

#printing elements at specified indices
indexed_arr=arr[[1,1,0,3],[3,2,1,0]]

print("Prints the elements at indices(1,3),(1,2),(0,1),(3,0)", indexed_arr)


