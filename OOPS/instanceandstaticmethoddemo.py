class MysecondClaas:
    def m1(self):# if we are not specifying @staticmethod it is instance method
        print("this is instance method")

    @staticmethod
    def m2(): # for static method no need to specify self keyword , its openatinoal
        print('This is a static method')
    
    @staticmethod
    def m3(self): # for static method no need to specify self keyword  if we specify when ever we are calling that method we need tp pass arguments also coz static method treats self as a parametre
        print('This is a static method',self)


mc = MysecondClaas()

mc.m1()  # for instance method no need to provide any arguments to self

MysecondClaas.m2()  # here calling static method directly using class not through object
MysecondClaas.m3("mk")
