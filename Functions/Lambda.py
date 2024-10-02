# this is normal function
def add(a):
    return a + 100

print(add(10))


x = lambda a :a + 100  #here lambda means syntax and a is variable like argument for that a we are putting colon and writing a again and adding + 100

print(x(10))



x = lambda a ,b:a *b
print(x(2,6))



x = lambda a ,b,c:a *b + c
print(x(2,6,3))