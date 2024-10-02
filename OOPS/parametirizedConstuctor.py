# ex 08 constructor arguments
name = 'Yemme'  # global variable

class mySeventClass:
    name = "jhon"  # class-level variable

    def __init__(self, name):  # parameterized constructor
        print(self.name)  # prints the class-level variable 'jhon'
        print(name)  # prints the passed argument 'Mani'
        print(globals()['name'])  # again prints the class-level variable 'jhon'

mc = mySeventClass("Mani")  # passing parameter to constructor



class Employee:
    def __init__(self,empid,empname,empsalary) -> None:
        self.empid = empid
        self.empname = empname
        self.empsalary = empsalary
        
    def Display(self):
        print(self.empid,self.empname,self.empsalary)
    
    
emp = Employee(101,'Mk',5000)
emp.Display()
emp1 = Employee(102,'Mkk',588000)
emp1.Display()

# ex 10   additional Constructor for printing only string data

class emp1:

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def __str__(self): # here wr are just returning the String type of data
        return self.name


e1 = emp1(100001, "JhacACAon", 2000000)
print(e1) # if we want to print that string data just we need to print object reference
