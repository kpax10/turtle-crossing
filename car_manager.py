from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1, 2)
        self.setheading(180)
        self.y_cor = random.randint(-250, 250)
        self.goto(290, self.y_cor)

    def move(self):
        for _ in range(10):
            new_x = self.xcor() - MOVE_INCREMENT
            self.goto(new_x, self.y_cor)
        # self.forward(STARTING_MOVE_DISTANCE)
        # self.forward(STARTING_MOVE_DISTANCE)
        # self.forward(STARTING_MOVE_DISTANCE)
        # self.forward(STARTING_MOVE_DISTANCE)


# TODO 2: Create cars that are 20px high by 40px wide that are randomly generated along
#  the y-axis and move to the left edge of the screen. No cars should be generated in
#  the top and bottom 50px of the screen (think of it as a safe zone for our little
#  turtle). Hint: generate a new car only every 6th time the game loop runs. If you
#  get stuck, check the video walkthrough in Step 4.