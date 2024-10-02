# if we have same names for variables how to invoke
a, b = 10, 40


class A:
    a, b = 54, 55  # Class variables for A


class B(A):
    a, b = 69, 88  # Class variables for B

    def add(self, a, b):  # Local variables
        print(a + b)  # Sum of local variables a and b (5 + 3)
        # Sum of class variables a and b of class B (69 + 88)
        print(self.a + self.b)
        # Sum of inherited class variables from class A (54 + 55)
        print(super().a + super().b)
        # Sum of global variables a and b (10 + 40)
        print(globals()['a'] + globals()['b'])


bobj = B()
bobj.add(5, 3)
