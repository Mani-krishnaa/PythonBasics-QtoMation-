
# ex=03
class mySecondThree:
    a, b = 10, 20  # class variables

    def add(self):
        # print(a,b) # we cannot access class variable directly
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)


mc = mySecondThree()  # creating object of class
mc.add()
mc.mul()

# ex = 04  # defining class global local variables

i, j = 15, 25  # global variables


class myfourthClass:
    a, b = 54, 8  # class variables

    def add(self, x, y):  # here x, y are local variables
        print(x + y)  # x,y are local variables
        print(self.a, self.b)  # with the help of self we can acees class variables inside a method
        print(i, j)  # global variables


mc = myfourthClass()

mc.add(100, 200)

# ex = 05  # here for global and local variable  im giving same name


a, b = 15, 25  # global variables


class myfifthClass:
    a, b = 54, 8  # class variables

    def add(self, a, b):  # here x, y are local variables
        print(a + b)  # x,y are local variables
        print(self.a, self.b)  # with the help of self we can acees class variables inside a method
        # print(a, b) here we cannot acces global variable when names are same
        print(globals()['a'] * globals()['b'])  # now it will able to acess global variables outside the class


mc = myfifthClass()

mc.add(100, 200)
