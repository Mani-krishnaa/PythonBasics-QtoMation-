def enterNum(num):
    if num < 0:
        raise ValueError("Only Integers are allowed")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


enterNum(10)
enterNum(3)
try:
    enterNum(-1)
except:
    print("Handled")
