from polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, height, width) -> None:
        super().__init__(height, width)

    # def getArea(self):
    #     return super().getArea()
    
    # def getPerimeter(self):
    #     return super().getPerimeter()
    
rectangle1 = Rectangle(10, 4)

print(rectangle1.getArea())