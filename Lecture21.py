'''
inheritance : deriving the attribute 
of some other class
types of inheritance
single 
multilevel
hierarchical
multiple
hybird
'''

# single inheritance

class Employee:
    def __init__(self,emp_name,salary):
        self.emp_name=emp_name
        self.salary=salary

    def login(self):
        print(self.emp_name +" Logged IN")


class Tester(Employee): #inheritance
    def test_code(self):
        print(self.emp_name ," test the software")

t1=Tester("Jamshed",80000)
t1.login()
t1.test_code()

t2=Tester("laxmi",120000)
t2.login()
t2.test_code()

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def product_details(self):
        print("product name is "+self.name)
        print("product price is "+str(self.price))

class Mobile(Product):
    def show_ram(self):
        print(self.name + " has 2 gb ram")


M1=Mobile("iphone",150000)
M1.product_details()
M1.show_ram()