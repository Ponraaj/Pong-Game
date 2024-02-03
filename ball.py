from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_value = 10
        self.y_value = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_value
        new_y = self.ycor() + self.y_value
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_value *= -1

    def bounce_x(self):
        self.x_value *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.move_speed = 10
        self.x_value *= -1