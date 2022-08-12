"""Public,Private,Protected Access Specifier"""
# public
# protected
# private

class Employee:
    no_of_leaves=0
    public=4
    _protect=90#protectet var mate 1_
    __private=100#private var mate 2_
    def __init__(self,aname,asalery,arole):
        self.name=aname
        self.salery=asalery
        self.role=arole

    def printdetails(self):
        return f"Employee name is {self.name}, salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        # params=string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good " + string)


emp=Employee("mayur",345,"programmer")
print(emp._protect)
print(emp._Employee__private)