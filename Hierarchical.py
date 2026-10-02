class BaseClass:
    def open_browser(self):
        print("browser opens")
    def close_browser(self):
        print("close broswer")
class Login(BaseClass):
    def user_login(self):
        print("user logged in")

class addCart(BaseClass):
    def add_to_cart(self):
        print("added to cart")

class SignUp(BaseClass):
    def register(self):
        print("user sign up")

class MainClass(Login,addCart,SignUp):
    def main(self):
        print("this is main class")

m1=MainClass()
m1.open_browser()
m1.user_login()
m1.add_to_cart()
m1.register()
m1.close_browser()
