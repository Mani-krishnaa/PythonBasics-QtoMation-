# ex 10   additional Constructor, it will return the value in string format

class emp1:

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def __str__(self): # here wr are just returning the String type of data
        return f"Employee Name: {self.name}, Employee ID: {self.eid}"



e1 = emp1(100001, "JhacACAon", 2000000)
print(e1) # if we want to print that string data just we need to print object reference