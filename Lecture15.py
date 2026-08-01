
def sub_list(li,start,end): 
    new_list=[]
    for i in range(start,end+1):#3 4
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