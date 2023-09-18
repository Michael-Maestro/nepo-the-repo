import turtle
# squar 
class TurtleMike(): # This class holds the data necessary to make the turtle so that you can draw shapes! Yay!
    def __init__(self, color): 
        self.pencil = turtle.Turtle()
        self.pencil.color(color)
class square(TurtleMike): #This is a square
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        self.pencil.forward(100) # Forward goe forward
        self.pencil.left(120)
        self.pencil.forward(100) # left goes Left
        self.pencil.left(120)
        self.pencil.forward(100)
    # Octagon! We found a glorious octagon!
class idk(TurtleMike):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        for i in range(8):
            self.pencil.right(45)
            self.pencil.forward(50)
        self.pencil.right(135)
        self.pencil.forward(100)

    # Circle but it displays the like circumfereradius or whatever.
class circle(TurtleMike):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        self.pencil = turtle.Turtle()
        self.pencil.circle(100)
        self.pencil.goto(0,100)
        self.pencil.forward(100)
        self.pencil.goto(0,100)
        self.pencil.back(100)
        self.pencil.goto(0,100)
        self.pencil.left(90)
        self.pencil.forward(100)
        self.pencil.goto(0,100)
    # i Definitely a Rhombus.
class rombis(TurtleMike):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        self.pencil.forward(100)
        self.pencil.right(45)
        self.pencil.forward(100)
        self.pencil.right(135)
        self.pencil.forward(245)
        self.pencil.right(135)
        self.pencil.forward(100)
    #i think im bad at code
class doesntwork(TurtleMike): #Diamond Attempt.
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        self.pencil.right(45)
        for i in range(4):
            self.pencil.forward(100)
            self.pencil.right(90)
        self.pencil.goto(0,-140)
        self.pencil.right(135)
        self.pencil.back(69)
        self.pencil.right(90)
        self.pencil.forward(71)
        self.pencil.back(133)

TurtleMike = idk("blue", 100)
TurtleMike.draw()