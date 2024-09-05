#inheritance example for behaviour of diffrent animals
#single inheritance - only inherit one base class
# multiple inherutance - inerit multiplebase classes
    # must be inside brackets,separated by comma
    #class Derivedclasss(base class1, base class2)

#multilevel inheritance - yes, connecting in a few
class Animal():
    def eat(self):
        print("I can Eat")

    def sleep(self):
        print('I can sleep')
    

#derive a class
class Dog(Animal):
    def bark(self):   
        print('I can bark') 

#create a dog object that accesses all the members of the Animal class
#call it simba
simba = Dog()
simba.eat() #calling from the main

simba.sleep() # calling from the main class
simba.bark() #calling from the derived class

#create anew class for a cat inherits the behaviour of animal 
#try accessing the behaviour of dog

class Cat(Animal):
    def mews(self):   
        print('I can mews') 



cat = Cat()
cat.eat()
cat.sleep()
cat.mews()


class Germanshephard(Dog):
    def protect(self):
        print("I am a protector")

bruno = Germanshephard()
bruno.bark()
bruno.sleep()
bruno.eat()
bruno.protect()
