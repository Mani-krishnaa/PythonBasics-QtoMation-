# Ex 01

# to define function we will use special keyword called def

def myfun():
    print("Hello")


# to call the function, just cl the function name

myfun()


# Ex 02 passing single parameter

def myfun1(name):
    print("Hello", name)


myfun1('mani')


# Ex 03 passing double parameter

def cal(a, b):
    return a * b


sum = cal(10, 20)
print(sum)


# ex04 if we return nothing it will print none

def fun():
    return


print(fun())


# ex05

def fun4():
    i = 10


print(fun4())
