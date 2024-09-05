# classs computer
# '__' BEFORE A VARIABLE CREATES APRIVATE VARIABLE
class Computer():
    def __init__(self):
        self.__maxprice = 900 # this price is only accessible inside the 

    def sell(self):
        print('selling price: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

C = Computer()# creating an object of the class computer
ConnectionError.sell # accessing the sell function under Computer

#modify the price

C.__maxprice = 1000
C.sell()


C.setMaxPrice(1000)
C.sell()

#Encapsulation = data hiding
#private attributes

#we use a sinle or double underscore to identify a private attribute

# polymorphism - takea many forms
#same entity(method, or operator or object) performing different operation
#different scenarios

class Polygon(): #this is our seperclass
    #create amethodnto render a shape
    def render(self):
        print('Rendering a polygon...')

#create a class to create a square out of the polygon

class Square(Polygon):
    #render the square
    def render(self):
        print('Rendering a square...')

#class to create a circle out of the polygon 

class Circle(Polygon):
    #render the circle

    def render(self):
        print("Rendering a circle...")

#create an object of the square

s1 = Square()
s1.render()

#create an object of circle and assign render method

c1 = Circle()


