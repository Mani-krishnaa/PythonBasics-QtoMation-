print("This is Starting Point")
print("This is Starting Point")
print("This is Starting Point")
try:
    print(x)
except:
    print("Exception occured")

print("End of programee")
print("End of programee")
print("End of programee")

try:
    print(2/0)
except:
    print("We cannott divide number by 0")



#ex3 multiple except block  , try , except esle , finally
try:
    num, num1 = 2,"dfghj"
    result = num1 / num
except Exception:
    print("Thrwon syntax error")
else:
    print("result is ", result)
finally:
    print("Finally Block Excuted")