from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, x_cord, y_cord):
        super().__init__()
        screen = Screen()
        self.x_cord = x_cord
        self.y_cord = y_cord
        screen.tracer(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 0.3)
        self.goto(self.x_cord, self.y_cord)

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
