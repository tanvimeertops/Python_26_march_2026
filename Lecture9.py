#Print the Digits of Number '459' in reverse order
# print : 9 5 4
# N=459
# while(N>0):
#     print(N%10,end=" ") #5
#     N=N//10 #4
    

#Print sum of digits of N. N > 0
# N = 6531
# 6+5+3+1 = 15.	print(15)
N=6531
sum=0
while(N>0):
    rem = N%10 #6%10=5
    sum =sum+rem #1+3+5+6
    N=N//10 #6

print(sum) #15
#Add a given digit to the back of a given number N
N=24
D=148
#1356
print(N*10**len(str(D))+D) # 10 
# print(N*100+D)

#reverse a given number N
copy=-256
if copy<0:
    N=copy*-1
else:
    N=copy
rev=0
while(N>0):
    D=N%10 #1
    rev=rev*10+D #531
    N//=10
if copy<0:
    print(rev*-1)
else:
    print(rev) #531

