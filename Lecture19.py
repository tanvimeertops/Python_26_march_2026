# import sys
# encoding=sys.getdefaultencoding()
# print(encoding)

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