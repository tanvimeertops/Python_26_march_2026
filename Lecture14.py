students= ['kusum','Shubham','pooja','kashish','Shio','uruj']
#         #       0     1        2
# print(students[2])
# print(len(students)) #3
# #reverse indexing
# num=[1,2,3,4,5]

# print(students[-2])

# #Updating an Index in a List
# students[1]="Naveen"
# print(students)
# students[-1]="piyush"
# print(students)

# #Iteration in a List
# #for each
# #for var_name in range(len(list_name))

# #method 1
# for index in range(3):
#     #range 0 n-1
#     #0 1
#     print(students[index],end=" ")
# #method 2
# for n in num:
#     print(n,end=" ")

# a = [1,2,3,4]
# for index in a:
#     print(index*index)

# a = [1,2,3,4]
# for index in range(len(a)):
#     a[index]=a[index]**2 #a[2]=a[2]**2
# print(a)

#Functions in a List
#append()
# a=[]
# print(a)

# a.append(10)
# print(a)
# a.append(True)
# print(a)
# a.append("jamshed")
# print(a)
# a.append("jamshed")
# print(a)

# #insert()
# a.insert(1,"nayana")
# print(a)
# a.insert(0,"laxmi")
# print(a)
# a.insert(-1,"manish")
# print(a)
# a.insert(101,"nancy")
# print(a)

# #pop()
# print(a.pop())

# print(a.pop(0))

# print(a.pop(-1))

# #print|(a.pop(101))
# print(a)

# students.remove('pooja')
#print(students)

#+ operator
a=[1,'q',2]
b=[4,5,6]
print(a+b)

#extend
a=[2,3,4,7]
a.extend(['a',5,9,6])
a.extend(range(5))
print(a)

#in operator
a=['a','c','d','g']

print('c' in a)
print('f' in a)

if 'f' in a:
    a.remove('d')

print(a)

#*	How to take List as Input

colors=[]
n =int(input("enter no of color :"))
for _ in range(n):
    color=input("enter color :")
    colors.append(color)
print(colors)

#find the index

a=['piyush','shekhar']

for i in range(len(a)):
    if a[i]=='shekhar':
        print(i)

a=['a', 'b', 'c']
for i in range(len(a)): #
    print(i,'     ',a[i] )
