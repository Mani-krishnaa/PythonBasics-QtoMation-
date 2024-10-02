# basically enumarates gives index and values
# enumarate() function on list

fruits_list = ['apple', 'bananna', 'cherry']

fruits_enum = enumerate(fruits_list)
for index, fruits in fruits_enum:
    print(index, fruits)


# enumarate() function on list
my_string = 'Hello'


my_StringEnmu = enumerate(my_string,start=0) # here start is optinal if we didint specify it will take from 0 if we specify from thier it will start index

# for index,char in my_StringEnmu:
#     print(index,char)

# we can directly put in a list also
print(list(my_StringEnmu))

