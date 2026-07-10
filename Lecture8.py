count = 0    # count=0
while(count < 10): #0 to 9 10<10
    print(10, end = ' ')  # 10 10 10 10 10 10 10 10 10 10 10
    count += 1 # 1 2 3 4 5 6 7 8 9 10

count = 1 # 1
while(count <= 5): # 2<=5
    if(count == 2): #2==2
        break
    print(count, end = ' ') #1 
    count += 1 #2
#Check Whether a Number is Prime or Not ?
#  Prime -> factor exactly equal to 2
# 5 3 7 11
# If a N is not divisble by any number between 2
#  and N-1 then it is a prime number
# N=5 2 to 4 
# N=6 2 to 5

N=int(input("Enter a number: ")) #6
flag=False #False
if N==1: 
    print(N,"is not a prime number")
elif N==2:
    print(N,"is a prime number")
else:
    for i in range(2,N): #2 to 5
        if N%i==0: # 6%2==0
            flag=True
            break
    if flag==True:
        print(N,"is not a prime number")
    else:
        print(N,"is a prime number")