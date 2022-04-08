from Shape2D import Shape2D
class Square(Shape2D):

    def __init__(self, color, side):
        Shape2D.__init__(self, color)

        self.side = side

    def getSide(self):
        return self.side

    def setSide(self, side):
        self.side = side

    def computeArea(self):
        return self.side ** 2

    def computePerimeter(self):
        return self.side * 4

    def getShapeProperties(self):
        return "Shape: SQUARE, Color: {}, Side: {}, Area: {}, Perimeter: {}" \
               .format(self.color, self.side, self.computeArea(),
                       self.computePerimeter())
