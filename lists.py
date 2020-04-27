# items in the list need not to be of the same type

# accessing values in the list
demo_list1 = ['python', 'java', 'c', 'c++', 1,2,4,5]
demo_list2 = [1,3,4,7,8,9,5]
print('list[2]:', demo_list1[0])
print('list[1:5]', demo_list2[1:5])

# updating lists
demo_list2[3]=99

# deleting list elements
del demo_list1[1]

# finding the length
print(len(demo_list1))

# concatenating the lists
print(demo_list1+demo_list2)

# repetition
print(['hey, there']*4)

# iteration
for i in demo_list2:
    print(i)


