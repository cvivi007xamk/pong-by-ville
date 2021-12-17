# In this file we define tha classes used in the app

import functions
from constants import *
import pygame
import math
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


# A class Box that generates different color, size and position having boxes
class Box:

    def __init__(self, color, width: int, height: int, position: tuple):
        # We encapsulate all of the attributes
        self.__color = color
        self.__width = width
        self.__height = height
        self.__position = position

# Boxes have a method show that draws them on pygame screen
    def show(self):
        pygame.draw.rect(
            screen, self.__color, (self.__position[0] - self.__width/2, self.__position[1] - self.__height/2, self.__width, self.__height), 1)

# A getter that returns box outlines in pixel position (order left, top, right, bottom). This is used in the is_inside funtion.
    @property
    def outlines(self):
        return (self.__position[0] - self.__width/2, self.__position[1] - self.__height/2, self.__position[0] + self.__width/2, self.__position[1] + self.__height/2)

# A getter for the center of a box
    @property
    def center(self):
        return (self.__position[0], self.__position[1])

# Make a Ball class that generates new balls that have attributes like direction, size, speed etc.


class Ball:

    def __init__(self, color, direction: int, speed: float, radius: int, position: tuple):
        self.color = color
        self.__direction = direction
        self.__speed = speed
        self.__radius = radius
        self.__position = position
        self.__hits = 0

# Balls also have a show method that draw them on screen
    def show(self):
        pygame.draw.circle(screen, self.color, self.__position, self.__radius)

# Let's make some getters to make our life easier in the future (we need the y-positions, directions and so on)
    @property
    def y_position(self):
        return self.__position[1]

    @property
    def position(self):
        return self.__position

    @property
    def direction(self):
        return self.__direction

# Balls also have collide method that changes their direction
    def collide(self, side):
        if side == "top" or side == "bottom":
            self.__direction = 180 - self.__direction

        if side == "right" or side == "left":
            self.__direction = 360 - self.__direction
            self.__hits += 1
            # Here we use the mandatory recursive function to add speed to a ball every time a paddle hits it. The function itself is defined in the funtions.py file.
            self.__speed = functions.recursive_speed_addition(
                self.__speed, self.__hits)

# Balls also have a move-method that changes their position according to the angle it is moving and the speed of which it is moving.
    def move(self, paddle1, paddle2):
        degree = 0.0174532925
        angle = (self.__direction - 90)*degree
        x = self.__position[0]
        y = self.__position[1]
        x_new = x+math.cos(angle)*self.__speed
        y_new = y+math.sin(angle)*self.__speed
        # If the move-method would make the ball collide with a paddle or a screen edge we call the collide method of the ball to deal with that.
        if y_new - self.__radius < 0:
            self.collide("top")
        elif y_new + self.__radius > screen_height:
            self.collide("bottom")
        elif x - self.__radius > paddle1.position[0] + paddle_width/2 and x_new - self.__radius < paddle1.position[0] + paddle_width/2 and y_new <= paddle1.bottom + 2 and y_new >= paddle1.top - 2:
            self.collide("left")
        elif x + self.__radius < paddle2.position[0] - paddle_width/2 and x_new + self.__radius > paddle2.position[0] - paddle_width/2 and y_new <= paddle2.bottom + 2 and y_new >= paddle2.top - 2:
            self.collide("right")
# Otherwise we set a new position to the ball
        else:
            self.__position = (x_new, y_new)
# We also have a del method (as every object has) to delete the balls that go in a goal. To make sure that happens we print a Ball deleted text to the console.

    def __del__(self):
        print('Ball deleted.')

# We have a paddle class too


class Paddle:
    # We encapsulate all attributes to make them so that we don't accidentally change them.
    def __init__(self, color, length: int, position: tuple, is_computer: bool):
        self.__color = color
        self.__length = length
        self.__position = position
        self.__is_computer = is_computer
        self.__top = self.__position[1] - self.__length / 2
        self.__bottom = self.__position[1] + self.__length / 2
# Let's make some getters

    @property
    def y_position(self):
        return self.__position[1]

    @property
    def position(self):
        return self.__position

    @property
    def is_computer(self):
        return self.__is_computer

    @property
    def bottom(self):
        return self.__bottom

    @property
    def top(self):
        return self.__top
# And also we have a methos to set the top and bottom attributes, because we need to do that separately when position is changed.

    def set_top_and_bottom(self):
        self.__top = self.__position[1] - self.__length / 2
        self.__bottom = self.__position[1] + self.__length / 2

# Paddles have move_paddle methods that change their position and also call the method that sets the top and bottom points.
    def move_paddle(self, direction, speed):
        if direction == "up" and self.__top - speed >= 0:
            self.__position = (self.__position[0], self.__position[1] - speed)
        if direction == "down" and self.__bottom + speed <= screen_height:
            self.__position = (self.__position[0], self.__position[1] + speed)
        self.set_top_and_bottom()

# And we also have a show method that draws the paddles on the screen with pygame
    def show(self):
        pygame.draw.line(screen, self.__color, (self.__position[0], self.__top), (
            self.__position[0], self.__bottom), paddle_width)
