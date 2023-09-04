import turtle
# squar
class TurtleMike():
    def __init__(self, color):
        self.t = turtle.Turtle()
        self.t.color(color)
class square(TurtleMike):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        self.t.forward(100)
        self.t.left(120)
        self.t.forward(100)
        self.t.left(120)
        self.t.forward(100)
    # glorious
class idk(TurtleMike):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        for i in range(8):
            self.t.right(45)
            self.t.forward(50)
        self.t.right(135)
        self.t.forward(100)

    # circle but with math stuff i did math ages ago
class circle(TurtleMike):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        self.t = turtle.Turtle()
        self.t.circle(100)
        self.t.goto(0,100)
        self.t.forward(100)
        self.t.goto(0,100)
        self.t.back(100)
        self.t.goto(0,100)
        self.t.left(90)
        self.t.forward(100)
        self.t.goto(0,100)
    # i forgot what shape this is
class rombis(TurtleMike):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        self.t.forward(100)
        self.t.right(45)
        self.t.forward(100)
        self.t.right(135)
        self.t.forward(245)
        self.t.right(135)
        self.t.forward(100)
    #i think im bad at code
class doesntwork(TurtleMike):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length
    def draw(self):
        self.t.right(45)
        for i in range(4):
            self.t.forward(100)
            self.t.right(90)
        self.t.goto(0,-140)
        self.t.right(135)
        self.t.back(69)
        self.t.right(90)
        self.t.forward(71)
        self.t.back(133)

doesntwork.draw()