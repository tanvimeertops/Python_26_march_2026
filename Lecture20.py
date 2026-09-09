#class : blueprint
#class : keyword
#name of the class Car
#pass : when class body is unknown or empty,
#  we use pass to avoid error
#pass : it is a placeholder that does nothing
#object : instance of a class
#object : it gives permission to access 
# functionality of the class
#self : it is a reference to the 
# current instance of the class
class Car:
    pass
    def initialize(self):
        print("Hello")
    
car1=Car() #object1 of class Car
car1.initialize()
#Car.initialize(car1) #object1 of class Car
# car2=Car() #object2 of class Car
#_init_: to initialize the class variable
# class Bag:
    
#     def __init__(self,name):
#         self.name=name
#         print("This bag belongs to ",self.name)

# s1=Bag("John")
# s2=Bag()
#constructor : it is a special function 
# that is automatically called when an object of the 
# class is created. 
# It is used to initialize the attributes of the class. 
# The constructor method is defined using the 
# __init__() method.
class Bag:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        print(name)
        print(color)
b1=Bag("John","Blue")

class Bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

customer1=Bank("John",1000)
customer2=Bank("Alice",2000)

print("customer name :" + customer1.name)
print("customer balance :" + str(customer1.balance))

print("customer name :" + customer2.name)
print("customer balance :" + str(customer2.balance))

class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

P1=Product("laptop",150000,15)
P2=Product("Mouse",1500,150)

print("product name is "+P1.name)
print("Price is "+str(P1.price))
print("Stocks "+str(P1.stock))

print("product name is "+P2.name)
print("Price is "+str(P2.price))
print("Stocks "+str(P2.stock))