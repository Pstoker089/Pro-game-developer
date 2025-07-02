#parent class
class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def printer(self):
        print(f"name of person is {self.name}")
        print(f"ID of person is {self.id}")
#child class
class employee(person):
    def __init__(self, name, id,salary,role):
        super().__init__(name, id)
        self.salary=salary
        self.role=role
    def details(self):
        print(f"the sallary of the person is {self.salary}")
        print(f"the role of the person is {self.role}")

p1=person("Greg",518)
e1=employee("Greg",518,"£500/h","Financial manager")
p1.printer()
e1.details()
        