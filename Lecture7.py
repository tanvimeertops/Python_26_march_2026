count=0
while count<5:
    count+=1
    if(count==3):
        print(count," Absent")
        continue
        
    print(count,"  present")
   
order_no=0
while order_no<5:
    order_no+=1
    if(order_no==3):
        print(order_no,"  Cancelled")
        continue
        
    print(order_no,"  Delivered")

print(list(range(5)))#0 to 4
print(list(range(-5))) # 0 to n-1 jump +1
print(list(range(0)))
print(list(range(1))) #0

print(list(range(1,3))) #1 2 
print(list(range(-5,-1))) #-5 -4 -3 -2
print(list(range(-4, -10))) #-4 -5 -6 -7 -8 -9
print(list(range(10,5))) #10 to 6

print(list(range(1,6,2))) # 1 to 5 1 3 5
print(list(range(0, -5, -1))) #0 -1 -2 -3 -4
print(list(range(-5, 0, 1))) # -5 -4 -3 -2 -1
print(list(range(0,5,1))) #0 1 2 3 4
print(list(range(-5,-10,-1))) #-5 -6 -7 -8 -9

for num in range(10):
    print(num+1)

for num in range(100):
    print(num,end=" ")