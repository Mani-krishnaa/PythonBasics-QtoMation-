class A:
    sum = 100  # public variables
    __sum1 = 320  # private variable for this we need to create one method inside the class , inside that method with self keyword we can acess
    
    def display(self):
       print(self.__sum1)
       


a = A()
print(a.sum)
a.display()
# print(a.__sum1)


class B:
    def mydisplay(self):  # public methods
        print('mydisp')

    def __mydisplay1(self):  # private methods
        print('mydisp1')

    def mydisp3(self):
        self.__mydisplay1()


# for private methods we can acess inside inside the class so we need to create on more method and with the help og self keyword we can private method
b = B()
b.mydisplay()
b.mydisp3()
