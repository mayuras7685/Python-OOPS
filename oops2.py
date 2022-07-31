class Employee:
    no_of_leaves=9 #class variables
    pass
mayur=Employee()
rohin=Employee()

mayur.name="mayur"#instance of variables
mayur.salary=455
mayur.role="software eng."

rohin.name="rohin"
rohin.salary=403
rohin.role="communication eng."

print(rohin.no_of_leaves)
Employee.no_of_leaves=11
print(mayur.no_of_leaves)
mayur.no_of_leaves=12
print(mayur.__dict__)
print(rohin.__dict__)
print(Employee.__dict__)