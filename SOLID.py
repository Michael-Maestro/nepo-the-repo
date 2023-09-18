"""
SOLID is a set of principles that are used in coding.
SOLID is in itself a word that states multiple different terms with their own meanings.
1 - The S in SOLID stands for the Single Responsibility Principle - "A module should be responsible to one, and only one, actor." 
What this infers is that modules (pieces of code) should only be allowed to do what is asked of them.
2 - The O in SOLID stands for the Open-closed Principle - "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification."
This means that code can be freely added to without having to alter the source code.
3 - THE L in SOLID stands for the Liskov substitution principle -  "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."
I don't know what a pointer is, but it's pretty important.
4 - The I in SOLID stands for the Interface segregation principle - "Clients should not be forced to depend upon interfaces that they do not use."
This simply means everything should have its place in essence; people shouldn't have to rely on other pieces of technology to achieve their unrelated end.
5 - The D in SOLID stands for the Dependency inversion principle - "Depend upon abstractions, [not] concretions."
This means that modules and code should depend on abstractions of code instead of non-changeable 'bad' code.
"""

# SOLID: 
# Single Responsibility Principle (SRP):
# Each class (Circle, Square, AreaCalculator, App) has one specific role, as per S of SOLID.
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
