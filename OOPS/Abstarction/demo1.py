# Abstract class with multipl abstarct method

from abc import ABC, abstractmethod

# Abstract class


class Shape(ABC):

    # Abstract method 1
    @abstractmethod
    def area(self):
        pass

    # Abstract method 2
    @abstractmethod
    def perimeter(self):
        pass


# Concrete class: Rectangle
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing abstract method area
    def area(self):
        print(self.width * self.height)

    # Implementing abstract method perimeter
    def perimeter(self):
        print(2 * (self.width + self.height))


r = Rectangle(10,20)
r.area()
r.perimeter()
