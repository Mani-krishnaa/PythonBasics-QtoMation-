class A:
    def m1(self):
        print("This is from M1 class A")


class B(A):
    def m1(self):
        print("This is from M1 class B")
        super().m1()
        


b = B()
b.m1()  # it will give child  method
         # but i want PArent methods also on that time we need write super() along method name
