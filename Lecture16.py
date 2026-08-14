# list of planets
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# print(planets)
# planets.append("Pluto")
# print(planets)

# tuples of number 
num = (1,2,3)
# print(num)
# print(type(num))
# num[0]=0
# print(num)

# a=()
# print(a)
# print(type(a))

# a=('a',)
# print(a)
# print(type(a))

# 1 to 10
# numbers = tuple(range(1, 11))
# print(numbers)
# numbers.append(11)
# print(numbers)

# a=[]
# for i in range(1, 11):
#     a.append(i)
# print(a)
# a=tuple(a)
# print(a)

# Tuples in functions 
# def swap(a,b):
#     return b,a

# # print(swap(1,2))
# print(type(swap(1,2)))
# a,b=swap(1,2)
# print(a)
# print(b)

# def name():
#     first_name=input("Enter your first name: ")
#     last_name=input("Enter your last name: ")
#     return first_name, last_name

# fisrt,last=name()
# print(fisrt)
# print(last)

# a=(1,2,3,[4,5,6])
# print(a)
# a[0]=9
# print(a)
# a[-2]=7
# print(a)

# a[3].append(7)
# print(a)

# a=(1,2,3,4,5,78,12,90,100)
# # for n in a:
# #     print(n)

# for i in range(len(a)):
#     print(a[i])

#String
# a="Piyush"
# b='singh'
# print(type(a))
# print(type(b))
# #a[0]="S"
# print(a)

#char to ascii
# print(ord('a'))
# print(ord('D'))
# print(ord('2'))
# print(ord('*'))

# #ascii to char
# print(chr(65))
# print(chr(75))
# print(chr(95))
# print(chr(105))

# a=["Naveen","Piyush","Rohit"]
# a[0]="Praveen Kumar"
# print(a)

# # a=a+24
# # print(a)
# a=a+'d'
# print(a)

a="tops"
for char in a:
    print(char)

name="Piyush"
name1="piyush"

print(name==name1)

text = "Tops Technologies"
print(text[0:6]) #Tops
print(text[-3:]) #ies
print(text[6:11]) #echno
print(text[::-1])
print(text[::2])#Tp o e h l i e
print(text[3:])

# Functions in strings
print("tops".capitalize()) #Tops technologies
print('tops tech'.title())
print('tops tech'.count('t')) #2
print('pooja makhija'.count('ja'))
print('tops tech'.replace('t',"delta"))
a='piyush'
print(a.replace('i','e'))
a='piyush singh'
print(a.replace('i','e',1))
print('abc_bncd_def'.split('_'))#returns list
a = ['abc', 'bncd', 'def']
print('+_'.join(a)) #abc_bncd_def
print('tops tech'.upper()) #TOPS TECHNOLOGIES
print('TOPS TECHNOLOGIES'.lower()) #tops technologies

name = 'Piyush' 
gender= 'Male' 
age = '30'
print("Name :",name,"Gender :",gender,"Age :",age)
print(f'name:-{name} gender:-{gender} age:-{age}')
temp="Name : {} Gender : {} Age : {}"
print(temp.format(name,gender,age))

# List Comparison
print([1,2,3,4,5]<[1,3])
print([1,3,0]>[1,3])
print([1,3]==[1,3])
print([1,4,5]>[1,6])
#String comparison
print('a'<'A') #97<65
print('Aakar'>'Sudip') #65 

# You are given a list of strings, 
# where each string represents a log entry 
# from a system. 
# # Your task is to find and print all log entries 
# that contain the word "ERROR".

# logs = [
#	"2024-07-18 10:00:01 INFO Server started",
#	"2024-07-18 10:01:17 ERROR Failed to connect to database", #	"2024-07-18 10:02:45 WARNING High memory usage",
#	"2024-07-18 10:04:10 ERROR Disk full",
#	"2024-07-18 10:06:30 INFO Backup complete" # ]

logs = [
"2024-07-18 10:00:01 INFO Server started",
"2024-07-18 10:01:17 ERROR Failed to connect to database", #	"2024-07-18 10:02:45 WARNING High memory usage",
"2024-07-18 10:04:10 ERROR Disk full",
"2024-07-18 10:06:30 INFO Backup complete" ]

for log in logs:
    if "ERROR" in log:
        print(log)

# Question 2 -> Print the longest line 
lines = [
  "DevOps is awesome.",
  "Error: Disk not found.",
  "Server started successfully at 10:05 AM.",
  "OK"
]

# longest_line=''
# for line in lines:
#     if len(line)>len(longest_line):
#         longest_line=line
    

# print(longest_line)

# print(max(lines))

# #list comprehension
# row =5
# col = 10

# arr=[ [ 0 for _ in range(col)]for _ in range(row)]
# print(arr)
# for _ in range(row):
#      for _ in range(col):
#          print(0,end=" ")
#      print()

b =[ 
    [1,5],
    [2,3]
   ]
row=len(b) #2
col=len(b[0]) #2
c=[[0 for _ in range(col)] for _ in range(row)]
print(c)

# for i in range(row):
#     for j in range(col):
#         c[j][i]=b[i][j]
# print(c)
