#if you do not know how many arguments that will be passed into your function, add a * before the parametre name in the  function definition
#this function will recive a tuple of arguments, and can acess the items accordingly


def my_function(*kids):
    print(kids)
    print(kids[1])
    print(kids[3])
    
    
    

my_function('jackhgjh','debg',1,'df3grthy','e23rght')