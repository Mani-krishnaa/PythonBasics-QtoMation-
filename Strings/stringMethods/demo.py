# create string variable single or double qoutes are fine


# ways of creating strings variables
s = "welcome"
s = 'welcome'

s = str('dsvewg')
s = str("dsvewg")

# i want to crate a string variable but i dont want to store anything

name = str()
name = ""
name = ''

# mutuable we can the change the value of the variable
# immmutuable we cannot the change the value of the variable

str1 = "Welcome"  # if we want to print the adress of variable id is the method
print(id(str1))

str1 = str1 + "to python"
print(id(str1))
# if the value is changed after updation themn it is immmutable

# how to use + and * with strings

str = 'welcome'
print(str + 'prmnbvmlc;')

print(str * 2)  # it will print 2 times of string

# how to use SLICE [] with strings
# strating index starts from 0
# ending index starts from 1
str = 'welcome'

print(str[1:5])  # elco
print(str[:6])  # welcom, by defualt it is starting index is zero
print(str[2:])  # lcome, be defualt ending value will take whole string

print(str[1:-1])  # elcom , here it will remove last char

# how to use ord()  and chr()
# ord id used to return the asci value of the characters

print(ord('A'))  # 65
# char is used to return the character ie we provide sci number

print(chr(65))  # A

# how to use min()  and max() and len()

print(max("abc"))  # c

print(min("abc"))  # a

print(len("ManiKrishna"))  # 11

# how to use in , notin operator

s = 'welcome'
print("come" in s)  # in opeartor returns  true
print("lome" in s)

print("come" not in s)  # in opeartor returns false
print("lome" not in s)

# testing strings true/ false
s = 'welcome to python'
print(s.isalnum())  # it will check the string contins number or not
print("MAni".isalpha())  # it will check only alphabets

print(s.isdigit())  # checks for digit

print(s.isidentifier())  # it will check the identifiers are present in string or not

print(s.islower())
print(s.isupper())

print("  ".isspace())

# searching for substring

s = 'welcome to python'
print(s.endswith("thon"))
print(s.startswith("we"))
print(s.find("com"))  # return staring index where its started
print(s.find("zz"))  # return -1 if not present

print(s.count("o"))  # count the chars

print(s.capitalize())
print(s.upper())
print(s.lower())

print(s.swapcase())  # if we have upper it will connct lower vice cersa

print(s.replace("on", "in"))

# reverse a astring

s = "Mani"
rev_str = ''
# method 1 using loops

for i in s:
    rev_str = i+rev_str
print(rev_str)

# method 2

s= 'krishna'
rev_str = s[::-1]
print(rev_str)

