class mysixthclass:

    def __init__(self) -> None:
        print('Constructor')

    def m1(self):
        print("Hello")

    def m2(self, x, y):
        return x + y


mc = mysixthclass()  # here at the time of object creation only constructor gets invoked and it will call automatically also
mc.m1()  # method we have to cl explicit by using object
print(mc.m2(10, 7))
