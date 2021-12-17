# We need pretty much all the constants so let's import them all
from constants import *

# Let's pass the parameters from the start screen


def show_mygame(player1_is_computer, player2_is_computer, computer1_level, computer2_level, paddle1_color, paddle2_color):

    from text import smallfont, text_player1, text_player2
    from classes import Paddle
    from functions import new_ball
    import pygame
    from end_screen import show_end_screen

# Initializi pygame and fill screen
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(black)

# The new_ball function is defined in the functions.oy file. It creates a new ball with random direction
    ball = new_ball()

# Make new paddles as objects of the Paddle class. They have the set colors and other parameters.
    paddle1 = Paddle(paddle1_color, 80,
                     (10, screen_height/2), player1_is_computer)
    paddle2 = Paddle(paddle2_color, 80, (1190, screen_height/2),
                     player2_is_computer)

    pygame.display.set_caption("Pong by Ville")
    clock = pygame.time.Clock()

# Let's set soem of the variables that are needed here.
    paddle1_up = False
    paddle1_down = False
    paddle2_up = False
    paddle2_down = False

    player1_score = 0
    player2_score = 0

# We also need to display the score at the top of the screen so let's make the necessary variables for displaying those
    text_player1_score = smallfont.render(str(player1_score), True, red)
    player1_score_rect = text_player1_score.get_rect()

    player1_score_rect.center = (2.5*grid_width, 0.2*grid_height)

    player1_rect = text_player1.get_rect()
    player1_rect.center = (2*grid_width, 0.2*grid_height)

    text_player2_score = smallfont.render(str(player2_score), True, red)
    player2_score_rect = text_player2_score.get_rect()
    player2_score_rect.center = (6.5*grid_width, 0.2*grid_height)

    player2_rect = text_player2.get_rect()
    player2_rect.center = (6*grid_width, 0.2*grid_height)

# Also set the winner (both false at the start)
    player1_won = False
    player2_won = False

# We run a while loop for the game (at 60hz)
    game = True

    while game:
        for e in pygame.event.get():
            # The arrow up/down and the w/s keys move the paddles
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    paddle2_up = True
                if e.key == pygame.K_DOWN:
                    paddle2_down = True
                if e.key == pygame.K_w:
                    paddle1_up = True
                if e.key == pygame.K_s:
                    paddle1_down = True

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_UP:
                    paddle2_up = False
                if e.key == pygame.K_DOWN:
                    paddle2_down = False
                if e.key == pygame.K_w:
                    paddle1_up = False
                if e.key == pygame.K_s:
                    paddle1_down = False

            if e.type == pygame.QUIT:
                exit()

# Fill the screen with black as a start of every refresh.
        screen.fill(black)

# We define the ball.move method in the classes.py file where the Ball class is defined. It moves the ball between refreshes.
        ball.move(paddle1, paddle2)
        # If the ball goes beyond the paddles/screen we record the goal and delete the ball (as to not have the object going on outside of the screen for eterneity.) Also we make a new ball with the new_ball function.
        if ball.position[0] < -50 and player2_score < 5:
            player2_score += 1
            del ball
            # If the score is five we have a winner and break out of the while loop.
            if player2_score >= 5:
                player2_won = True
                game = False
            ball = new_ball()
        if ball.position[0] > screen_width + 50 and player1_score < 5:
            player1_score += 1
            del ball
            if player1_score >= 5:
                player1_won = True
                game = False
            ball = new_ball()

# here we draw the score text on the screen
        text_player1_score = smallfont.render(str(player1_score), True, red)
        text_player2_score = smallfont.render(str(player2_score), True, red)

        screen.blit(text_player1, player1_rect)
        screen.blit(text_player2, player2_rect)
        screen.blit(text_player1_score, player1_score_rect)
        screen.blit(text_player2_score, player2_score_rect)

# If the aforementioned keys are pressed we move the paddles. Paddle objects have move method in them that changes their position.
        if paddle2_up:
            paddle2.move_paddle("up", 5)
        if paddle2_down:
            paddle2.move_paddle("down", 5)
        if paddle1_up:
            paddle1.move_paddle("up", 5)
        if paddle1_down:
            paddle1.move_paddle("down", 5)

# If one of the players is a computer we move their paddles automatically to follow the ball. The chosen difficulty level defines the speed by which the paddles move.
        if player1_is_computer:
            if paddle1.y_position < ball.y_position:
                paddle1.move_paddle("down", 1 + 0.5 * computer1_level)
            if paddle1.y_position > ball.y_position:
                paddle1.move_paddle("up", 1 + 0.5 * computer1_level)

        if player2_is_computer:
            if paddle2.y_position < ball.y_position:
                paddle2.move_paddle("down", 1 + 0.5 * computer2_level)
            if paddle2.y_position > ball.y_position:
                paddle2.move_paddle("up", 1 + 0.5 * computer2_level)

# Let's show the ball and paddles (they both have methods that show them)
        ball.show()
        paddle1.show()
        paddle2.show()

        pygame.display.flip()

        # Refresh rate is 60hz because we have moving objects
        clock.tick(60)

# After we break the loop we run the end screen function and pass the winner as parameter.
    show_end_screen(player2_won, player1_won)
