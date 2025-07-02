class bird():
    def intro(self):
        print("There are birds")
    def flight(self):
        print("Most birds can fly, some cannot")
class fly(bird):
    def flight(self):
        print("Sparrows can fly")
class no_fly(bird):
    def flight(self):
        print("penguins cannot fly")

b=bird()
f1=fly()
f2=no_fly()
b.intro()
b.flight()
f1.intro()
f1.flight()
f2.intro()
f2.flight()
