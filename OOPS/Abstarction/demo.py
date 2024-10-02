from abc import ABC, abstractmethod

# Abstract class with one abstarct method
class Animal(ABC):
    
    # Abstract method (no implementation)
    @abstractmethod
    def sound(self):
        pass

# Subclass 1
class Dog(Animal):
    
    # Implementing the abstract method
    def sound(self):
        return "Woof Woof"

# Subclass 2
class Cat(Animal):
    
    # Implementing the abstract method
    def sound(self):
        return "Meow Meow"

# Driver code
dog = Dog()
print(dog.sound())  # Output: Woof Woof

cat = Cat()
print(cat.sound())  # Output: Meow Meow
