# python decorators
# it  is a function that takes in a function and return it by adding some Functionality

def extra_greetings(func):
    def inner():
        print('Good Morning')
        func()  # here im calling the function the is parametre of extra_greetings
    return inner


@extra_greetings
def simple_greetings():
    print('Hello Qtomation')

# we can call in 2 ways
# 1 approcach

# decoratedGretings = extra_greetings(simple_greetings)
# decoratedGretings()


# 2 approach we need use @ and function name like  @extra_greetings
simple_greetings()


# multiple decoratos

def Shivani(func):
    def yemme():
        print('Yemme TARA MAdbeda')
        func()
    return yemme


def Meghana(func):
    def paytm():
        print('Paytm karo')
        func()
    return paytm


@Shivani
def mohsin():
    print('Mohsin')


@Meghana
@Shivani
def mani():
    print('Mani')


mohsin()
mani()
