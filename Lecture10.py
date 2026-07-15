'''
*****
*****
*****
*****

'''
for _ in range(4):#0 to 3
      print('* '*5)
    
'''
*       1
**      2
***     3
****    4
*****   5

'''

for i in range(1,6):
      print('*'*i)

'''
++++*
+++**
++***
+****
*****
'''
row=5
for i in range(1,row+1):
      spaces=' '* (row-i)
      star="*"*i
      print(spaces+star)

'''
+++*
++* *
+* * *
 * * *
++* *
+++*

'''
row=3
for i in range(1,row+1): # 1 2 3 
      spaces=' '* (row-i)
      star="* "*i
      print(spaces+star)
for j in range(row-1,0,-1): #   1
      spaces='+'* (row-j) # 3-1 2 
      star="* "*j #* 
      print(spaces+star) #++* 
'''
    *
   ***
  *****
   ***
    *
'''
row=3
for i in range(1,row+1): # 1 3  
      spaces=' '*(row-i)
      star="*"*(i*2-1)
      print(spaces+star)
    
for i in range(row-1,0,-1): # 1 3  
      spaces=' '*(row-i)
      star="*"*(i*2-1) # *
      print(spaces+star)