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

mayur=Employee("mayur",455,"DM")
mohit=Employee("mohit",450,"M")

mayur.change_leaves(34)
print(mayur.salary)
print(mayur.no_of_leaves)