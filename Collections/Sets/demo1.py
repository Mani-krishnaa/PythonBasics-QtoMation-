# Set --unordered and unindexed , set is MUTABLE
# creating Set

mySet = {"apple", "banana","banana", "cherry", 1, 2, 3, 5} # Duplicates are not allowed


#we  cannot modify extisting values but we can add or remove
mySet.add('Mango') # adding
mySet.add('Kiwi')

print(mySet)

mySet.remove("cherry")
# checking presence

if "apple" in mySet:
    print(True)
else:
    print(False)
# accesing set , we cannot acees index bcoz we doesnt have index concepts its unindexed

for i in mySet:
    print(i)


# we can add two sets and here we can add tuple list also
myset1 = {'rghn','dsfadgsf','qdfgd'}

mySet.update(myset1)


myTupple = ('apple', 'bannana', 1, 2, 4, 5, 6, 4, 'cherry',
            'Sapota', 'kiwi', "efefe3", '43f43f4f')

mylist = ['apple', 'mango', 'bannana']

mySet.update(myTupple)
mySet.update(mylist)
print(mySet)


#clear all items from set
mySet.clear()
print(mySet) # it will clear all items but it wont delete the set


# del mySet
# print(mySet)
