#single inheritance
class Employee:
    no_of_leaves=11
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"Employee name is {self.name}, salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_str(cls,string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good "+ string)

class programmer(Employee):
    no_of_holidays=23
    def __init__(self,aname,asalary,arole,languages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=languages

    def printprog(self):
        return f"Employee name is {self.name}, salary is {self.salary} and role is {self.role}.The languages are {self.languages}"



mayur=Employee("mayur",455,"DM")
mohit=Employee("mohit",450,"M")

milan=programmer("milan",555,"programmer",["python"])
arjun=programmer("arjun",675,"programmer",["cpp","ruby"])

print(milan.printdetails())
print(milan.printprog())