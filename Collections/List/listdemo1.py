mylist = ['apple', 'mango', 'bannana']
mylist1 = [10, 20, 30, 40, 50]

print(mylist)

# change values
mylist[0] = 'kiwi'
print(mylist)


# checking the presence of element
if 'mango' in mylist:
    print(True)
else:
    print(False)

# 08: i want add new item
mylist.append("ManiKrishna")  # if we use append it will at last
print(mylist)
mylist.insert(0, "Yemme")  # it will add in between with the help of index
print(mylist)

# remove item from list
mylist.pop()
mylist.pop(0)
print(mylist)

# here del command removes single item based on the index , del is a keywrd not a function
del mylist[1]
print(mylist)

mylist1.clear()
print(mylist1)


# copying list
# 1 using copy()

# mylist3 = ['apple', 'mango', 'bannana',10, 20, 30, 40, 50]

# mylist4 = mylist3.copy()
# print(mylist4)

# 2 using list method

mylist3 = ['apple', 'mango', 'bannana', 10, 20, 30, 40, 50]

mylist4 = list(mylist3)
print(mylist4)


# 3 using airthmatic opeartor

mylist5 = ['apple', 'mango', 'bannana', 101, 202, 303, 404, 505]

mylist6 = mylist3 + mylist5
print(mylist6)

# using for loops

mylist7 = ["c++", "java", "Selenium"]

for i in mylist6:
    mylist7.append(i)
print(mylist7)


# sorting

mylist8 = ["c", "java", "Selenium", 'apple', 'mango', 'bannana']
print(mylist8)
mylist8.sort()
mylist8.sort(reverse=True)
print(mylist8)
