#To invoke parent class constructor

class A:
    def __init__(self):
        print('we are inside method m1 from class A')


class B(A):
    def __init__(self):
        print('we are inside method m2 from class B')
        # super().__init__() # approach 1
        A.__init__(self) # approach 5


b = B()
