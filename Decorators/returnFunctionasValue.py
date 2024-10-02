# retrun function as a value
def greetings(name):
    def hello():
        return "Hello " + name
    return hello


greet = greetings("Mani Krishna")
print(greet())
