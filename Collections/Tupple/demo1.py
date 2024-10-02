# creating tupple
myTupple = ('apple', 'bannana', 1, 2, 4, 5, 6, 4, 'cherry',
            'Sapota', 'kiwi', "efefe3", '43f43f4f')
mytupple1 = tuple()  # emptyTupple
mytupple2 = ()  # emptyTupple

# when we are creating tupple if we having only one item we need to comma, if we didnt specify it will treat it as string
mytupple3 = ("str",)
print(type(mytupple3))

# printing tupple
print(myTupple)


# aceesing tuple items
print(myTupple[1])
print(myTupple[-1])

# checking presence of items
if 'apple' in myTupple:
    print(True)
else:
    print(False)

# accesing range of values

print(myTupple[2:5])
# printing all items

for i in myTupple:
    print(i)
# changing tupple items
 # we cannot change or modify
#  we cannot insert
# we cannot remove

# changing the tuple values by defualt we cannot do coz it is immutable but indirect way we can
# we can convert into list again we can convert list into tuple

mylist = list(myTupple)  # list is used to convert any thing into list
mylist[0] = 'dihfiewnf'
mylist.append('gddddddddd')
myTupple = tuple(mylist)  # tupple is used to convert am=ny thing i to tupple
print(myTupple)


#counting lenth

print(len(myTupple))

# copy of touple we can do bcoz we are just copying we are not modifying
mytuppl1=myTupple
print(mytuppl1)

# we can delete tupple
del mytuppl1
# print(mytuppl1)

# can we join 2 tupples

myTupple3 = (1,5,8,2,5,58,2)

myTupple4 = myTupple3 + myTupple

print(myTupple4)

# comparing two tupples
if myTupple==myTupple4:
    print(" equal")
else:
    print("Not equal")


# we can multiply tupple
myTupple5 = ('apple', 'bannana' ,'kiwi','kiwi', "efefe3", '43f43f4f')
print(myTupple5 * 2)


#count = it will count occurance of particular value
print(myTupple5.count("kiwi"))

#index = return the index of particular value
print(myTupple5.index("kiwi"))