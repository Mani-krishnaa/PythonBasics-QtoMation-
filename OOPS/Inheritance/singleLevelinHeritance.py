#single level one parent and one child class
class A:
    def m1(self):
        print("Method m1 is called from Class A")

class B(A):
    def m2(self):
        print("Method m2 is called from Class B")

b = B()

b.m1()  # inherited from Class A
b.m2()  # called from Class B




class B:
    x, y = 10, 20

    def m1(self):
        print(self.x, self.y)


class C(B):
    a,b = 1000,200

    def m2(self):
        print(self.a-self.b)


c =C()
c.m1()
c.m2()