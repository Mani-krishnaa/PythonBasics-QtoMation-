# class num:
#     def add(self, a):
#         print(a)

#     def add(self, a, b):
#         print(a+b)

#     def add(self, a, b, c):
#         print(a+b+c)


# n = num()
# n.add(20, 30, 40)
# n.add(10)

# here it will take only the latest methods it will perform for a+b+c, but i wont support for remaing 2 methods


# for this problem we have approches

class A:
    def add(self, a=None, b=None):
        if a != None and b == None:
            print(a)
        else:
            print(a+b)
#in this 

a = A()
a.add(10)
a.add(10, 20)




class Humann:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")


h = Humann()
h.sayHello("Scott")
h.sayHello()


class calucaltion:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)


c = calucaltion()
c.add()
c.add(10, 20)
c.add(10, 20, 30)
