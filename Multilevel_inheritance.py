# class Employee:
#     def __init__(self,emp_name):
#         self.emp_name=emp_name
#     def login(self):
#         print(self.emp_name+ " logged IN")
# class Developer(Employee):
#     def write_code(self):
#         print("developer write code")

# class Tester(Developer):
#     def test_code(self):
#         print("Tester test code")


# t1=Tester("Jamshed")
# t1.login()
# t1.write_code()
# t1.test_code()


# class BaseClass:
#     def open_browser(self):
#         print("browser open")
#     def close_browser(self):
#         print("broswer close")

# class Login(BaseClass):
#     def user_login(self):
#         print("user logged in")

# class Checkout(Login):
#     def logout(self):
#         print("User Logged out")


# c1=Checkout()
# c1.open_browser()
# c1.user_login()
# c1.logout()
# c1.close_browser()

class BaseClass:
    def open_browser(self):
        print("browser open")
    def close_browser(self):
        print("broswer close")

class ApiRequest:
    def send_request(self):
        print("api request send")

class Login(BaseClass,ApiRequest):
    def user_login(self):
        print("user logged in")


l1=Login()
l1.open_browser()
l1.send_request()
l1.user_login()
l1.close_browser()