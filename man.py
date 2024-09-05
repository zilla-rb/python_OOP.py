# import person
# #
# #create an object man from person

# man = person.person()# qualify the object we want to create from the class
# print(man.species)
# print(man.alive)

# #modify the alive status of the person to false

# person.alive = False
# print(man.alive)

# #give the man a name

# man.name = "Bronson"
# man.surname ="loni"
# print(man.name,man.surname)

class sample_class:
    def __init__(self, course):
     self.course = course
    def display(self):
        print(self.course)

object1 = sample_class("Python")
object1.display
