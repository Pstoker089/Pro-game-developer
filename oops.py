"""class Students:
    def __init__(self,name,age,grade,house,set,teacher):
        self.name=name
        self.age=age
        self.grade=grade
        self.house=house
        self.set=set
        self.teacher=teacher
        self.school="Cambride school"
    def printer(self):
        print(f"Name of student is {self.name}")
        print(f"Age of student is {self.age}")
        print(f"Grade of student is {self.grade}")
        print(f"House of student is {self.house}")
        print(f"Set of student is {self.set}")
        print(f"Teacher of student is {self.teacher}")
        print(f"School of student is {self.school}")

S1=Students("Tom",14,"A","Purple",1,"Mr Rogers")
print(S1.grade)
S1.teacher="Mrs Diamond"
S1.printer()"""

class food:
    def __init__(self,name,size,type,calories,origin,colour,group):
      self.name=name
      self.size=size
      self.type=type
      self.calories=calories
      self.origin=origin
      self.colour=colour
      self.group=group
    def printer(self):
       print(f"name of food is {self.name}")
       print(f"size of food is {self.size}")
       print(f"type of food is {self.type}")
       print(f"calories of food is {self.calories}")
       print(f"origin of food is {self.origin}")
       print(f"colour of food is {self.colour}")
       print(f"group of food is {self.group}")

f1=food("apple","16cm","fruit",150,"Asia","red","Fruits/Vegetables")

f1.printer()
