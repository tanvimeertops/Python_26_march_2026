# print(2==2)
# print(2==3)

# print(2==2.0)

# print(2=='2')
# print(1==None)
# print(2!='2')
# print('22'!='2')

# print("Tops"!='Tops')
# print('Abc'=="ABC")

# print(2>3)
# #print(2<'2')

# print(2<2.0000001)
# #print(2<None)

# print('a'<'b') 

# print('top'<'Tops') 
# print(100>=32)

# print(31<-43)

# print(31<=31)

# a=10
# a+=25#a=a+25
# print(a)

# a=75
# a/=2
# print(a)

# a*=2
# print(a)

# age=230
# print(age>20 and age<40)

# print('Top'=="Tops" and (-2<-3))
# print(not 'Tops'=="Tops")

a=3
a*=4
#a=a*4
print(a)

m_comp=120
m_culture='positive'
m_distance=300

g_comp =110 
g_culture = 'positive' 
g_distace = 30

# if(m_comp>80 and g_comp>80):
#     print("microsoft criteria filled")
# elif(g_comp>80):
#     print("google criteria filled")
# else:
#     print("sad life")

if(m_comp>80 and g_comp>80):
    if(m_distance<g_distace):
        print("Join Microsoft")
    else:
        print("Join Google")

#Problem Statement: Traffic Lights
# You have to ask about the color of the 
# traffic light from the user, if:

# it is green, then print go,
# it is yellow, then print wait, # it is red, then print stop
# green -> go
# yellow -> wait # red -> stop

# color =input("Enter the color of the traffic light: ")
# if(color=='green'):
#     print("go")
# elif(color=='yellow'):
#     print("wait")
# elif(color=='red'):
#     print("stop")

    # HW
# Problem Statement: Maximum of two
# Given two integers, print the maximum of them.
# a=20
# b=20
# if(a>b):
#     print(a)
# elif(b>a):
#     print(b)
# else:
#     print("Both numbers are equal")

num1=45
if(num1%2==0):
    print("Even")   
else:
    print("Odd")

# age=int(input("Enter your age: "))
# print(type(age))
# if(age>18):
#     print("You are eligible to vote")

# pis=float(input("Enter the value of pi: "))

# print(pis*2*2)


print(3*10/2) #30/2 =15

print(10-4/2)
#Q3
#(45%10)=> 5 # 5/2 => 2.5
print(45 % 10 / 2) 
print(True and not False)

a=30
if a > 10:
    print(a)
    if a % 5 == 2: 
        print('Bla')
else:
    print(a)
    print('1234')
