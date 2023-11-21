from polygon import Polygon

class Square(Polygon):
    def __init__(self, height):
        super().__init__(height, height)

square1 = Square(11)
print(square1.getPerimeter())
    