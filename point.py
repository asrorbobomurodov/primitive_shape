class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance_from_Xcoordinate(self):
        """
        This method finds the distance between a point and its X coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return self.y

    def distance_from_Ycoordinate(self):
        """
        This method finds the distance between a point and its Y coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return self.x

    def getQuadrant(self):
        """
        This method finds which quadrant the point is in.

        Args:
            No
        Returns:
            int: quadrant.
        """
        if self.x>0 and self.y>0:
            return "The point is in the First quadrant"
        elif self.x<0 and self.y>0:
            return "The point is in the Second quadrant"
        elif self.x<0 and self.y<0:
            return "The point is in the Third quadrant"
        elif self.x>0 and self.y<0:
            return "The point is in the Fourth quadrant"
        else:
            return "The point is in the line"

    def on_Xcoordinate(self):
        """
        This method checks for a point on the X coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return self.y == 0

    def on_Ycoordinate(self):
        """
        This method checks for a point on the Y coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return self.x == 0
    
point = Point(3,4)
print(point.on_Xcoordinate())
 