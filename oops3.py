#_self_ and __init__ class methods
class Employee:
    no_of_leaves=11
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"Employee name is {self.name}, salary is {self.salary} and role is {self.role}"


mayur=Employee("mayur",455,"DM")
mohit=Employee("mohit",450,"M")


# mayur.name="mayur"
# mayur.salary=40000
# mayur.role="CEO"
#
# mohit.name="mohit"
# mohit.salary=30000
# mohit.role="GM"

print(mayur.salary)