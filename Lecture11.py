def transaction_msg():
    print('*'*20)
    print("Transaction complete")
    print("Thank you")
    print('*'*20)


# print("hello")

# transaction_msg()

# def area_of_circle():
#     r=5
#     return(3.14*r*r)

# print(area_of_circle()+10)

# def sum():
#     a=10
#     b=34
#     return(a*b)

# print(sum()*10)

# # add grace marks 5 to all students

# #input: marks

# def getMarks():
#     return 56

# print(getMarks()+5)

# def get_discount(price):
#    return(price*5/100)
   
# price=int(input())
# print(price-get_discount(price))

# #gst 3%
# #salary+5000(bonus)

# def abc():
#     print('Hello')
#     return 
#     print("Tops")
#     return 'Tops'
# print(abc())

# def even_odd(no):
#     if no%2==0:
#         return 'even'
#     else:
#         return 'odd'
# print(even_odd(50))

#sum of 2 nos
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def calculate_salary_yearly(base_mothly,bonus,equity):
    yearly_base=mul(base_mothly,12)
    yearly_base_bonus=sum(yearly_base,bonus)
    total_salary=sum(yearly_base_bonus,equity)
    return total_salary

print(calculate_salary_yearly(35000,150000,40000)+10)


