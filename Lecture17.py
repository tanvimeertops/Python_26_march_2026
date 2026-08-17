# a={}
# print(type(a))

# a=2
# d={"admin":"tanvi",a:1, 'b':2 ,a:45.6}
# print(d)

# d={[1,2,3,4]:5}
# print(d)

# e={1:'a',True:1,(1,2):3,None:4}
# print(e)


nicknames = { "Madhuri": "Sweety",
"Vinoth": "Appu",
"Shubham": "Zoo Zoo",
"Kusum": "ku ku",
"Aakar": "Golu"
}
# print(nicknames[2])

print(nicknames['Kusum'])
print(nicknames['Vinoth'])
# print(nicknames['avp'])

print(nicknames.get("Aakar"))
print(nicknames.get('avp'))

print(nicknames.get('avp',"not present"))
print(nicknames.get('Kusum',"not present"))

a = {True: 'a', 'a': 1, 2: False, 3.14: 'pi'} 
print(a)
a[True]='b'
print(a)
a[False]=78
print(a)
a[False]=96
print(a)

nicknames["Kusum"]='new value'
print(nicknames)
print(len(nicknames))
del nicknames["Kusum"]
print(nicknames)