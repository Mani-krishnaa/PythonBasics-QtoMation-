# create dictinary
mydic = {
    101: "x",
    102: 'y',
    103: 'z',
    "brand": 'hundai',
    'year': 2021
}

print(mydic)

# acessing items

# 01
print(mydic["brand"])  # it will return value if we provide key

# 02 get()
print(mydic.get(103))

# changes values or update

print(mydic)
mydic["year"] = 2022
print(mydic)


# printing only keys
print(mydic.keys())

# printing only Values
print(mydic.values())


# read all items using loop
for x, y in mydic.items():
    print(x, y)


# i want check key is exist or not

if "year" in mydic:
    print("Exist")
else:
    print('not exist')

print("year" in mydic)  # we can write like this also

# find number of items
print(len(mydic))

# adding items to dictionary
mydic["color"] = 'red'
print(mydic)

# remove items to dictionary
# 01 using pop

mydic.pop("year")
print(mydic)

# 02 using del
del mydic[103]
print(mydic)

# copying dictionary

#01 without using copy method

mydic1=mydic
print(mydic1)

#02 with using copy method

mydic3=mydic.copy()
print(mydic3)


#clear the dic
mydic1.clear()
print(mydic1)


#del the dic

del mydic3
print(mydic3)
