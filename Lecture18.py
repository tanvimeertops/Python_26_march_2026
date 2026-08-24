s=set()
print(type(s))

s = {1,2,4,2,34,5,21,1,2}
print(s)

# s[1]=3
# print(s)
#True=1
#False=0
s={0,False,(1,2),'a'}
print(s)
# s={3,[1,2],False}

s.add(True)
print(s)

s.update(['d','e','f'])
print(s)

s.remove('a')
print(s)

print(len((s)))

for ele in s:
    print(ele)

print('e' in s)
print('k' in s)

food_that_you_like_to_eat = {'Pizza', 'Noodles', 'Pasta', 'Chocolates', 'Burger'} 
food_that_are_expensive = {'Pizza', 'Croissant', 'Avocado'}

print(food_that_you_like_to_eat.intersection(food_that_are_expensive))
print(food_that_you_like_to_eat.union(food_that_are_expensive))
print(food_that_are_expensive.difference(food_that_you_like_to_eat))
print(food_that_you_like_to_eat-food_that_are_expensive)

#remove duplicate words
sentence = 'This is a sentence. This is not a paragraph.' 
words=sentence.split(' ')
print(words)
unique_word=set(words)
print(unique_word)
print(len(unique_word))


logs = { 
    'server1_logs' : [ 
        {'timestamp': '2024-07-18 10:04:10', 'level': 'ERROR', 'message': 'Disk full'}, 
        {'timestamp': '2024-07-18 10:00:01', 'level': 'INFO', 'message': 'Server started'}, 
    ], 
    'server2_logs' : [ 
        {'timestamp': '2024-07-18 10:01:17', 'level': 'ERROR', 'message': 'Database connection failed'}, # Fixed missing }
        {'timestamp': '2024-07-18 10:02:45', 'level': 'WARNING', 'message': 'High memory usage'}, 
    ] 
}

merged_log=[]

for key,value in logs.items():
    # print(key)
    merged_log.extend(value)
print(merged_log)