class Myclass:
    def printName(self):
        print("inside printname method")
    def printEmail(self,email):
        print('email is ',email)
        
mk = Myclass()# this is object im stroing another variable this called named object we are storing in onther variable
print(id(mk)) #memory location
mk.printName()
mk.printEmail('mani@gmail.com')

Myclass().printName() # name less object