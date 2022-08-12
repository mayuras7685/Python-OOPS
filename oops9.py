#multiple inheritance
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


class player:
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetails(self):
        return f"The Name is {self.name}.Game is {self.game}"

class coolprogrammer(Employee,player):
        language="c++"
        def printlanguage(self):
            print(self.language)


mayur=Employee("mayur",455,"programmer")
rohin=Employee("rohin",555,"programmer")

dipak=player("dipak","football")
mohit=coolprogrammer("mohit",89999,"coolprogrammer")
