a=[1,2,3]
b=a
b[0]=5
print(a[0])
# not a copy 
#one list [1,2,3] a b

def outer_function(x):
    def inner_function(y):
        return x * y
    return inner_function

result=outer_function(3)(4)
print(result) 



