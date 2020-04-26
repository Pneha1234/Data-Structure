# is a container which can hold fix number of items of same type
# Element - Each item stored in an array
# Index - identifier of the location of an array
from array import *

# typecode- defines the type of value(i representing integer)
exm_array = array('i', [10,20,30,40,50])

# accessing array element
print(exm_array[2])

# inserting elements to the array
exm_array.insert(2,90)

# deletion in an array
exm_array.remove(40)

# update array
exm_array[3]=33

# Traverse
for i in exm_array:
    print(i)
