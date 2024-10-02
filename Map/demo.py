numbers = [1, 2, 3, 4, 5]  # i want square of this numbers

# defining funtion for square


def square(number):
    return number ** 2


 # syntax of map mao(function, iterables)
square_result = map(square, numbers)

# convert map to list to see the output
print(list(square_result))

# passsing multiple itreables
print('------------------------------')

number_list1 = [1, 2, 3, 4, 5]
number_list2 = [6, 7, 8, 9, 3]


def add(x, y):
    return x + y

add_result = map(add,number_list1,number_list2)

print(list(add_result))
