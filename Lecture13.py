#*	Positional and Keyword Arguments
def bio_data(name, age=0, gender=None):
    '''
    this function prints the biodata using information
    provided 

    Args:
    name
    age
    gender

    Return :None
   '''
    print("Name: ", name)
    print("Age: ", age) 
    print("Gender: ", gender)
bio_data("nayana",age=34)

print (round(3.45858,2))

def abc(a,b,c):
    print(a,b,c)
abc(10,20,30)

#syntax my_list=[element 1,element 2,element 3]

# a=[1,2,3]
# print(a)
# print(type(a))

# a=([1,2,3])
# print(a)

# b=['a','b','jamshed']
# print(b)

# a=[1,True,12.5,'Nayana',None]
# b=list(range(1,10,2))
# print(b)

students = ['Kusum', 'Shubham', 'Pooja']

#print(students[3])
print(students[-1])

print(students[len(students)-2])

students[1]="Naveen"
print(students)