import sys
encoding=sys.getdefaultencoding()
print(encoding)

# file=open("sample.txt","w+")
# file.write("This is \n multiple \n line")
# file.close()

# # file=open("sample2.txt","w+")
# # file.writelines(["1.tops\n" ,"2.Surat\n","3."])
# # file.close()

# file=open("sample.txt","r+")
# content=file.read(5)

# file.write("after \n file \n read")
# print(content)
# file.close()

# file=open("sample.txt","r+")
# content=file.readline()
# while content:
#     print(content)
#     content=file.readline()
# file.close()

# file=open("sample.txt","r+")
# content=file.readlines()
# print(content)
# file.close()

# f=open("demo.txt","w")
# f.write("Welcome \n to \nPython")
# f = open("demo.txt", "r+")

# cursor=f.readline()
# print(cursor)
# f.write("HELLO")
# try:
#     file=open("nbgfjkdsnhfgjkdsf.txt","r")
# except FileNotFoundError:
#     print("OOPs! File not found")

try:
    file = open('notes.txt', 'w') 
    file.write("This is a sample text file.\n")
    file.close()
    print('Write operation successful')
except PermissionError:
    print('Permission denied') 
except:
    print('Something went wrong in writing the file')

# file=open('notes.txt', 'r')
# #to print in console
# print(file.read())
# file.close()

with open('notes.txt', 'r') as file:
    print(file.read())

with open('input.txt', 'w') as file:
    file.write('This is line 1.\n') #1
    file.write('Room 202 has 4 ACs.\n') #4
    file.write('There are 3 dogs and 4 cats.\n') 
    file.write('ID: 007, Code: 123456')
    file.write('ID: 6')
    
    

max_digit=-1
result=""
with open('input.txt', 'r') as file:
    for line in file:
        digit_count = 0
        for character in line:
            if character.isdigit():
                digit_count+=1
        if digit_count > max_digit: #9>4
            max_digit = digit_count #9 
            result=line 
    print(line)    





    