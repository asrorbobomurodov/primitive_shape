from polygon import Polygon
from math import sqrt

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_possible(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a
    
    def getPerimeter(self):
        return self.a + self.b + self.c if self.is_possible() == True else False
    
    def getArea(self):
        p = self.getPerimeter() / 2
        return sqrt(p * (p-self.a) * (p-self.b) * (p - self.c)) if self.is_possible() == True else False
    
triangle1 = Triangle(3,4,5)
print(triangle1.getArea())
    
    