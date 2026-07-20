# area circle :3.14 *r*r

#input : radius
#process 3.14*r*r
#o/p :area of circle

# a=10 #global

# def area_circle(r):
#     area=3.14*(r**2) #local 
#     return area

# print(area_circle(2))
# print(a)
# print(area)

# a=1 #global
# def abc():
#     a=2 #loCAL
#     return a

# print(abc())
# print(a)

a=1 #global
def abc():
    global a #loCAL
    a=2
    return a

print(abc()) #2
print(a)# 2

def solve(a, b): 
    print('Function Started')
    return 0
    c = a + b 
    print('Function Ends')
c = solve(2, 3) 
print(c)
print(type(c))
# Simple interest
# take principal, rate and time as input from user 
#and create a function to calculate simple interest 
# # (p * r * t)/ 100

def simple_interest():
    p=int(input("Enter Principal :"))
    r=float(input("Enter rate :"))
    t=int(input("enter time :"))
    return (p*r*t)/100

si=simple_interest()
print(si)

