import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(key='w', fun=player.move)

counter = 0

game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    counter += 1
    if counter == 6:
        car = CarManager()

    # TODO 1: Counter not working


    # TODO 3: Detect when the turtle player collides with a car and stop the game if this happens

    # TODO 4: Detect when the turtle player has reached the top edge of the screen (i.e.,
    #  reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position
    #  and increase the speed of the cars. Hint: think about creating an attribute and using the
    #  MOVE_INCREMENT to increase the car speed

    # TODO 5: Create a scoreboard that keeps track of which level the user is on. Every time the
    #  turtle player does a successful crossing, the level should increase. When the turtle hits
    #  a car, GAME OVER should be displayed in the centre
