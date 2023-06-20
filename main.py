import random
import turtle as t
from scoreboard import Scoreboard
import time
from asteroids import Asteroid, asteroid_list
from spaceturtle import SpaceTurtle


def destroy_asteroids():
    for item in asteroid_list:
        if item.xcor() < -300:
            asteroid_list.remove(item)


# set up the board
screen = t.Screen()
screen.setup(width=600, height=500)
screen.bgpic("galaxymap.gif")
screen.title("Space turtle")
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()  # board = -200 to 200

# set up space turtle
space_turtle = SpaceTurtle()
screen.listen()
screen.onkeypress(space_turtle.move, "Up")

sleep_time = 0.2
generate_asteroid = False

game_on = True
while game_on:
    time.sleep(sleep_time)
    screen.update()
    # randomly generate asteroids or not
    generate_asteroid = random.choice(list([True, False, False, False]))
    if generate_asteroid:
        asteroid = Asteroid()
    for rock in asteroid_list:
        rock.move_asteroid()

    # check if space turtle got through the asteroid field
    if space_turtle.ycor() > 200:
        scoreboard.increase_score()
        space_turtle.start_position()
        sleep_time *= 0.9  # speed up asteroids

    # check if space turtle collided with the asteroid

    for rock in asteroid_list:
        # x_distance - how far away space turtle is from the asteroid on x_axis
        # rock.distance - how far away space turtle is from the asteroid on a y_axis
        # I could redo rock.distance to the same formula as x_axis but for this exercise rock.distance is enough
        asteroid_xcor = rock.xcor()
        turtle_xcor = space_turtle.xcor()
        x_distance = abs(turtle_xcor - asteroid_xcor)
        if x_distance < 20 and space_turtle.distance(rock) < 20:
            scoreboard.game_over_man()
            game_on = False

    destroy_asteroids()  # removes asteroids that passed screen boundry


screen.exitonclick()
