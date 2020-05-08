# tuples are the immutable objects of the python
# empty tuple a=()
# tuple with one object a=(b,)
#Accessing values in tuples
test_tup1 = ('a','b','c','d','e','f')
test_tup2 = (1,2,3,4,5,6,7,8)
print(test_tup2[1:3])
print(test_tup1[0])

# updating tuples
# Tuples are immutable which means you cannot update or change the values of tuple elements

# deleting tuple values
del test_tup1

#Basic Tuple Operations 
# Length
print(len(test_tup2))

#concatination
test_tup3=(2,3,4,5,6)
print(test_tup2+test_tup3)

#repetation
print(test_tup3*4)


# iteration
[print(i) for i in(1,2,3)]

