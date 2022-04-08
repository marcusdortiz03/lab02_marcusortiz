class Shape2D:

    def __init__(self, color):
        self.color = color.lower()

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color.lower()

    def getShapeProperties(self):
        return "Shape: N/A, Color: {}" \
               .format(self.color)

    
