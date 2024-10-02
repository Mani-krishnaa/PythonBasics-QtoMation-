def countDown(n):
    while (n > 0):
        yield n
        n = n - 1
        
#x is generator object
x = countDown(5)

# to print two ways

# 1  = next()
# print(next(x)) # here first 5 will print coz our condition will true so yild will stop the function snd give
# print(next(x)) # here again our condition is true and yiekd will stop function again and print 4
# print(next(x)) 
# print(next(x)) 
# print(next(x)) 

# 2 =  for in loop
#  num is a variable 
for num in x:
    print(num)