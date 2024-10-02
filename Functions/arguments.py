# ex 01

def fun(i, j):  # this is positional arguments coz while calling function first will take for i and second one for j
    print(i, j)


fun(10, 20)  # Positional arguments

fun(j=20, i=25)  # keyword arguments here we are explicit defining


# ex =02 : we can assign default values assigned to positional arguments

def fun1(i, j=10):
    print(i, j)


fun1(40)
fun1(20, 20)


# ex 03: keyword arguments

def arguments(name, grettings):
    print(grettings + "  " + name)


arguments(grettings='hello', name='jhon')
arguments(name='jhon', grettings='hello')
arguments('mani', 'wdwq')

# ex 04: keyword arguments


def my_fun(a, b, c):
    print(a, b, c)


my_fun(10, 20, 30)  # positinal parameter
my_fun(a=10, b=50, c=558)  # keyword parameter
my_fun(b=545, a=548, c=848)  # keyword parameter

my_fun(10, 20, c=45848)  # combination of positional and keyword


# my_fun(10,b=648974,84)# this is wrong as positional argument coz it must appear before any keyword argument
# my_fun(10,20, b=20) # this also wrong coz we are putting positional after keyword


# ex 05: function cal also return multiple statements

def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


res = largest(10000, 200)
print(res)
print(type(res))  # like this we can check the res iss which type of collection
