# as the name suggests abstract class is a class that is abstract in itself. It doesn't have the body of its own,
# instead inherits from its subclass. Also it enforces the sublasses to override the method, otherwise it will throw error


# from abc import ABCMeta, abstractclassmethod
from abc import ABC, abstractclassmethod


# class Shape(metaclass=ABCMeta):
class Shape(ABC):
    @abstractclassmethod
    def find_area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, len, bread):
        self.length=len
        self.breadth=bread
    def find_area(self):
        return self.length*self.breadth
    

r=Rectangle(2,11)
print(r.find_area())