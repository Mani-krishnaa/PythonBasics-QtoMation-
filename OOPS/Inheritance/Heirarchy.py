#hirerachy inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 100, 200

    def m2(self):
        print(self.a - self.b)


class C(A):
    i, j = 25, 25

    def m3(self):
        print(self.i * self.j)

c = C()
c.m1()
# c.m2() here we cannot write like this bcoz m2 method is extends to  c
c.m3()

b=B()
b.m2()
b.m1()
