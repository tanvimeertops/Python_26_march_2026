
def sub_list(li,start,end): 
    new_list=[]
    for i in range(start,end+1):#2 3
        new_list.append(li[i]) #li[2] 34 55 78
    return new_list # 



li=[2,14,34,55,78,26] #2 3 4 to 
print(sub_list(li,2,4))


new_list_slicing=li[2:5]
print(new_list_slicing) #34 55 78

my_list=[1,2,3,4,5,6,7,8,9]
print(my_list[2:7])
my_string="Hello python"
print(my_string[0:5])
print(my_string[:5])
print(my_string[7:])

print(my_list[0:10:2])

#reverse
print(my_list[::-1])
print(my_string[::-1])

#copy a list
my_new_list=my_list[:]
print(my_new_list)

a=[1,2,3]
b=a
a[2]=4

print(b)

math = [100, 98, 90] #0
science = [90, 100, 89] #1
hindi = [96, 76, 100] #2

subjects=[math, science, hindi]
print(subjects) #98

# Get the number of 2nd student for hindi 
print(subjects[2][1])
## Get the number of 3rd person for science subject 
print(subjects[1][2])

'''
100 98 90
90 100 89
96 76 100
'''
#*	Iterating a 2D list

for i in range(len(subjects)): #len(elements) row number
    for j in range(len(subjects[i])): #len(elements[i])no of col
        print(subjects[i][j],end=' ') #[2][0]= 90 100 89
    print()#new Line

#*	Input a 2d List
# user_input_2d_list=[]
# row=4
# col=2

# for i in range(row):
#     temp=[]
#     for j in range(col):
#         n=int(input())
#         temp.append(n)
#     user_input_2d_list.append(temp)
# print(user_input_2d_list)

# # Create a matrix of 5 (rows) * 4(column) 
# and enter only even numbers from 0 -> 40 
# # <!--
#	0	2	4	6
#	8	10	12	14
#	16	18	20	22
#	24	26	28	30
#	32	34	36	38
#	-->			

rows=5
cols=4
even_no=[]
count=0

for i in range(rows): 
    temp=[] # 0 
    for j in range(cols):
        temp.append(count) #0 2 4 6
        count+=2
    even_no.append(temp)

print(even_no)

a = [4 ,5 ,3,6, 10] 
n = 6

for i in range(len(a)):
    if a[i] == n:
        print("Element found at index", i)
        break
else:
    print("Element not found")

#index of the first occurrence of n in array 
#index()
a = [4 ,5 ,3,6, 10] 
n = 6
if n in a:
    print("Element found at index", a.index(n))
else:   
    print("Element not found")

#Given a list, you have to find the maximum element 
# in this list.

a = [2,10,2,12,60]
max_ele=a[0] #60
for i in range(1,len(a)):
    if a[i]>max_ele: #60>12
        max_ele=a[i] #60
print("Maximum element is", max_ele)

print(max(a))
print(min(a))