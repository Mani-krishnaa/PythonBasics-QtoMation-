class Employee:
    empname = 'jack'
    __salary = 2000
    
    def getsalary(self): # creating getter method
        print(self.__salary)
        
    def setSalary(self, salary): # creating setmethod
        self.__salary = salary

emp1 = Employee()
print(emp1.empname)
emp1.getsalary()
emp1.setSalary(200000)
emp1.getsalary()

