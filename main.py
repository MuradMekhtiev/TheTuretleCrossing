import time
from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.go_up, "Up")

car_manager = CarManager()

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:

        if player.distance(car) < 25:
            game_is_on = False

    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.next_level()

screen.exitonclick()