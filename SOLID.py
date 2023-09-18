"""
SOLID is a set of principles for writing better software code. It helps make code easier to understand, change, and maintain over time. 
Each letter in "SOLID" stands for a principle:

S: Single Responsibility Principle (SRP) - Each part of the code should do only one thing.
O: Open/Closed Principle (OCP) - Code should be open to adding new features but closed to changing existing ones.
L: Liskov Substitution Principle (LSP) - Substituting one part of code with another shouldn't break anything.
I: Interface Segregation Principle (ISP) - Code should use small and specific parts, rather than big and general ones.
D: Dependency Inversion Principle (DIP) - High-level parts of code shouldn't depend directly on low-level parts.

SOLID is important because it helps create code that's easier to work with, adaptable to changes, and less likely to have errors. 
It promotes good practices for designing software that's flexible, maintainable, and of high quality.
"""


# SOLID: 
# Single Responsibility Principle (SRP):
# Each class (Circle, Square, AreaCalculator, App) has one specific role.
class Shape:
    # Dependency Inversion Principle (DIP): High-level modules depend on abstractions (Shape), not on specific implementations.
    def area(self):
        pass

# Dependency Inversion Principle (DIP): Low-level modules (shape classes) implement those abstractions.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Liskov Substitution Principle (LSP): Circle and Square are both shapes and can be used interchangeably.
# Interface Segregation Principle (ISP): Square class only defines the methods it needs to calculate square area.
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class AreaCalculator:
    # Single Responsibility Principle (SRP): AreaCalculator calculates the area of different shapes.
    def calculate_area(self, shape):
        return shape.area()

class App:
    # Single Responsibility Principle (SRP): App runs the application.
    def run(self):
        circle = Circle(5)
        square = Square(4)
        
        calculator = AreaCalculator()
        circle_area = calculator.calculate_area(circle)
        square_area = calculator.calculate_area(square)
        
        print("Circle area:", circle_area)
        print("Square area:", square_area)

app = App()
app.run()

# Open/Closed Principle (OCP):
# You can easily add new shapes without changing existing code.
# The AreaCalculator can calculate areas of new shapes by extending the base Shape class.

# Liskov Substitution Principle (LSP):
# Circle and Square are both shapes and can be used interchangeably.

# Interface Segregation Principle (ISP):
# Each class defines only the methods it needs.

# Dependency Inversion Principle (DIP):
# High-level modules depend on abstractions (Shape), not on specific implementations.
# Low-level modules (shape classes) implement those abstractions.
