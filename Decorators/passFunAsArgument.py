# passing function as argument

def multiply(x, y):
    return x * y


def add(x, y):
    return x + y


def caluclate(function, x, y):
    return function(x, y)


result_multiply = caluclate(multiply, 20, 50)
result_add = caluclate(add, 20, 50)

print(result_multiply)
print(result_add)
