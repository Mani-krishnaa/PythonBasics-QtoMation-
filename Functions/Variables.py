# ex 01
global_var = 10  # globalVariable


def func():
    local_var = 10  # localVariable we cannot access outside the function
    print(global_var)
    print(local_var)


func()

# ex=02
#
# xy = 100 # global variable
#
# def cool():
#     xy=200 # localVariable
#     print(xy) # here it will refer local only
#
# cool()
# print(xy)# it will refer global only


xy = 100  # global variable


def cool():
    # global xy = 200 invalid we cant write like this
    global xy  # like this we can access and we can do modification
    xy = 200  # localVariable
    print(xy)  # here it will refer local only


cool()
print(xy)  # it will refer global only

# ex = 04
a = 100


def fun4():
    global a
    a = 500
    print(a)

fun4()
print(a)


# ex = 05

def fun5():
    global x # we can specify inside the function also global variable but we need to specify global
    x = 10.0
    print(x)

fun5()
print(x) # we can acces s outside also