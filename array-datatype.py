import numpy as np

#Detecting datatype as integer by numpy
a=np.array([1,2])
print("Datatype of a: ",a.dtype)


#Detecting datatype as float by numpy
b=np.array([11.2,2.3])
print("Datatype of b: ",b.dtype)

#Forced datatype int64
c=np.array([1.2,2],dtype=np.int64)
print("Datatype of C:", c.dtype )
print(c)

#Forced datatype float64
d=np.array([1.2,2],dtype=np.float64)
print("Datatype of D:", d.dtype )
print(d)

