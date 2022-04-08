from Shape2D import Shape2D
from Circle import Circle
from Square import Square 

# unchanging objects for testing
atomicShape = Shape2D("blue")
atomicCircle = Circle("blue",2.5)
atomicSquare = Square("blue",2.5)

# changeable objects for testing with expected values 
normalShape = Shape2D("blue")
normalCircle = Circle("blue",2.5)
normalSquare = Square("blue",2.5)

# objects for testing with stranger but acceptabe values 
shape0 = Shape2D("rAiNbOw")
circle0 = Circle("RAINBOW", 999)
square0 = Square("RAINbow", 999)

def test_setter_methods():
    normalShape.setColor("ReD")
    assert normalShape.color == "red"
    normalCircle.setColor("rEd")
    assert normalCircle.color == "red"
    normalCircle.setRadius(5)
    assert normalCircle.radius == 5
    normalSquare.setColor("RED")
    assert normalSquare.color == "red"
    normalSquare.setSide(5)
    assert normalSquare.side == 5

def test_getter_methods():
    assert normalShape.getColor() == "red"
    assert normalCircle.getColor() == "red"
    assert normalCircle.getRadius() == 5
    assert normalSquare.getColor() == "red"
    assert normalSquare.getSide() == 5
    
def test_calculation_methods():
    assert atomicCircle.computeArea() == 19.6349375
    assert atomicCircle.computePerimeter() == 15.70795
    assert atomicSquare.computeArea() == 6.25
    assert atomicSquare.computePerimeter() == 10.0

    assert circle0.computeArea() == 3135309.96159
    assert circle0.computePerimeter() == 6276.89682
    assert square0.computeArea() == 998001
    assert square0.computePerimeter() == 3996

def test_getProperties_methods():
    assert atomicShape.getShapeProperties() == "Shape: N/A, Color: blue"
    assert atomicCircle.getShapeProperties() == "Shape: CIRCLE, Color: blue, Radius: 2.5, Area: 19.6349375, Perimeter: 15.70795"
    assert atomicSquare.getShapeProperties() == "Shape: SQUARE, Color: blue, Side: 2.5, Area: 6.25, Perimeter: 10.0"

    assert shape0.getShapeProperties() == "Shape: N/A, Color: rainbow"
    assert circle0.getShapeProperties() == "Shape: CIRCLE, Color: rainbow, Radius: 999, Area: 3135309.96159, Perimeter: 6276.89682"
    assert square0.getShapeProperties() == "Shape: SQUARE, Color: rainbow, Side: 999, Area: 998001, Perimeter: 3996"