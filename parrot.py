class parrot:
    #attributes of the parrot

    name = ""
    age = 0

#create a parrot object 
#objectname = classname()

parrot1 = parrot() #parrot1 is our objest
#access the name attribute of the class and assign the parrot a name

parrot1.name  = "kimani machungwaa"
parrot1.age = 60

#create another object parrot2

parrot2 = parrot()
parrot2.name = "kalonzo mushoka"
parrot2.age = 68

#access the atttributes of each object
print(f"{parrot1.name} is {parrot1.age} years old")

print(f"{parrot2.name} is {parrot2.age} years old")

#we created a parrot class with two attributes (name and age)
#we then created 2 objects (instance of the class parrot)
# they referenced 


class simplest():
    pass
print("simplest is of type:", type(simplest))

#create an object of class simplest and check its type
simp = simplest()
print("simp is of type:" , type(simp))

#__main__.simplest - it indicates the name of the 
