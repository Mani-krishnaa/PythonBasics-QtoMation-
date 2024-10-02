#MultiLevel Inheritance where a class is derived from another class,
class A:
    def m1(self):
        print("Method m1 is called from Class A")

class B(A):
    def m2(self):
        print("Method m2 is called from Class B")
        
        
class C(B):
    def m3(self):
        print("Method m3 is called from Class c")

c = C()

c.m1() 
c.m2() 
c.m3()
