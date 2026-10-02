import re
# text = 'Title: Mrs. Lacy'

# pattern1=r'(Mr|Mrs|Ms)\.?\s[A-Z][a-z]+'

# match1=re.search(pattern1,text)
# print(match1)
# print(match1.group(1))



data ="""Dave Martin 615-555-7164
173 Main St., Springfield RI 55924 davemartin@bogusemail.com

Charles Harris 800-555-5669
969 High St., Atlantis VA 34075 charlesharris@bogusemail.com

Eric Williams 560-555-5153
806 1st St., Faketown AK 86847 laurawilliams@bogusemail.com

Corey Jefferson 900-555-9340
826 Elm St., Epicburg NE 10671 coreyjefferson@bogusemail.com

Jennifer Martin-White 714-555-7405
212 Cedar St., Sunnydale CT 74983 jenniferwhite@bogusemail.com

Erick Davis 800-555-6771
519 Washington St."""

# pattern="\d{3}-\d{3}-\d{4}"
# print(re.match(pattern,data))
# print(re.search(pattern,data))
#print(re.findall(pattern,data))
# numbers=re.finditer(pattern,data)
# for i,num in enumerate(numbers):
#     print(i,num)
#     if(i==5):
#         break

#enumerate()
# a=['a','b','c']
# for index,data in enumerate(a):
#     print(index,data)


# numbers=re.finditer(pattern,data)
# for i,num in enumerate(numbers):
#     print(num.group(),num.start(),num.end())

# pattern = '\d{3}'
# text = '123' 
# print(re.fullmatch(pattern,text))

# def validate_mobile(num):
#     pattern = r'\d{10}'
#     return bool(re.fullmatch(pattern, num))

# print(validate_mobile("788947483"))



# pattern=r'\b[A-Z][a-z]*\b'
# Text="A Tops Tech is in Surat"
# print(re.findall(pattern,Text))

# text = 'Started at 09:30, ended 13:00' 
# pattern=r'\d{2}:\d{2}(?::\d{2})?'
# print(re.findall(pattern,text))

# text= 'Running, testing, and logging complete.' 

# pattern=r'\b\w+ing\b'
# print(re.findall(pattern,text))

# text="ERR123 occurred after WARN456 and FAIL789" 
# pattern=r'\b(?:ERR|WARN|FAIL)\d+\b'
# print(re.findall(pattern,text))

text = 'Accessed 192.168.1.1 and 10.0.0.4'
pattern=r'\d{1,3}(?:\.\d{1,3}){3}'
print(re.findall(pattern,text))