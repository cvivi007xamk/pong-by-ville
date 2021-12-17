import random
from constants import *
from classes import Ball

# We make a separaet file where we have a few often used functions.

# This function checks if the first parameter is inside the second


def is_inside(position: tuple, box: object):
    if position[0] < box.outlines[0] or position[0] > box.outlines[2] or position[1] < box.outlines[1] or position[1] > box.outlines[3]:
        return False
    else:
        return True

# This function creates new balls that have random direction


def new_ball():
    ball_directions = [random.randint(20, 70), random.randint(
        110, 160), random.randint(200, 250), random.randint(290, 340)]
    ball_direction = ball_directions[random.randint(0, 3)]
    ball = Ball(red, ball_direction, 4, ball_radius,
                (screen_width/2, screen_height/2))
    return ball

# This functions sets the speed of the ball recursively after hitting a paddle. This would have been easier without recursion, but it was a mandatory thing to do so here it is.


def recursive_speed_addition(initial_speed, hits):
    if hits == 0:
        return initial_speed
    return 0.2 + recursive_speed_addition(initial_speed, hits-1)
