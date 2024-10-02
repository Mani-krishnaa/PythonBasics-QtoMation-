#examples for methods using super keyword
class A:
    def m1(self):
        print('we are inside method m1 from class A')


class B(A):
    def m1(self):
        print('we are inside method m2 from class B')
        super().m1()


b = B()
b.m1()  # it will give child  method
# but i want PArent methods also on that time we need write super() along method name


#examples for variables using super keyword

p, q = 10, 40  # global variables


class A:
    x, y = 54, 55  # class variables

    


class B(A):
    a, b = 69, 88  # class variables

    def add(self, m, n):  # local variables
        print(m+n)
        print(self.a+self.b)
        print(self.x + self.y) # it is inheritaed
        print(p+q)


b = B()
b.add(5,3) 