# This file and function shows the start menu
def show_start_screen():

    # Necessary imports from other files and modules
    from functions import is_inside
    import pygame
    from constants import screen_height, screen_width, grid_width, grid_height, black, white, red, yellow, green, blue
    import text
    from text import smallfont
    from classes import Box
    from mygame import show_mygame

# Set the screen size and fill with blavk
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(black)

# Name for the game window
    pygame.display.set_caption("Pong by Ville")
    clock = pygame.time.Clock()

# Here we set variables for the texts and get correct positions for them on the screen
# Also we want rectanqle buttons drawn around some text to denote clickability. We do make new boxes (of class Box here too).
    player1_rect = text.text_player1.get_rect()
    player1_rect.center = (2*grid_width, 1*grid_height)

    player2_rect = text.text_player2.get_rect()
    player2_rect.center = (6*grid_width, 1*grid_height)

    human1_rect = text.text_human.get_rect()
    human1_box = Box(white, 180, 100, (1*grid_width, 2*grid_height))
    human1_rect.center = (human1_box.center)

    computer1_rect = text.text_computer.get_rect()
    computer1_box = Box(white, 180, 100, (3*grid_width, 2*grid_height))
    computer1_rect.center = (computer1_box.center)

    human2_rect = text.text_human.get_rect()
    human2_box = Box(white, 180, 100, (5*grid_width, 2*grid_height))
    human2_rect.center = (human2_box.center)

    computer2_rect = text.text_computer.get_rect()
    computer2_box = Box(white, 180, 100, (7*grid_width, 2*grid_height))
    computer2_rect.center = (computer2_box.center)

    level1_rect = text.text_level.get_rect()
    level1_rect.center = (2*grid_width, 3*grid_height)

    level2_rect = text.text_level.get_rect()
    level2_rect.center = (6*grid_width, 3*grid_height)

    plus1_rect = text.text_plus.get_rect()
    plus1_box = Box(white, 80, 80, (3*grid_width, 4*grid_height))
    plus1_rect.center = (plus1_box.center)

    minus1_rect = text.text_minus.get_rect()
    minus1_box = Box(white, 80, 80, (1*grid_width, 4*grid_height))
    minus1_rect.center = (minus1_box.center)

    plus2_rect = text.text_plus.get_rect()
    plus2_box = Box(white, 80, 80, (7*grid_width, 4*grid_height))
    plus2_rect.center = (plus2_box.center)

    minus2_rect = text.text_minus.get_rect()
    minus2_box = Box(white, 80, 80, (5*grid_width, 4*grid_height))
    minus2_rect.center = (minus2_box.center)

    paddle_color1_rect = text.text_paddle_color.get_rect()
    paddle_color1_rect.center = (2*grid_width, 5*grid_height)

    paddle_color2_rect = text.text_paddle_color.get_rect()
    paddle_color2_rect.center = (6*grid_width, 5*grid_height)

    paddle1_box_yellow = Box(yellow, 80, 80, (0.5*grid_width, 6*grid_height))

    paddle1_box_green = Box(green, 80, 80, (1.3*grid_width, 6*grid_height))

    paddle1_box_red = Box(red, 80, 80, (2.1*grid_width, 6*grid_height))

    paddle1_box_blue = Box(blue, 80, 80, (2.9*grid_width, 6*grid_height))

    paddle2_box_yellow = Box(yellow, 80, 80, (5.1*grid_width, 6*grid_height))

    paddle2_box_green = Box(green, 80, 80, (5.9*grid_width, 6*grid_height))

    paddle2_box_red = Box(red, 80, 80, (6.7*grid_width, 6*grid_height))

    paddle2_box_blue = Box(blue, 80, 80, (7.5*grid_width, 6*grid_height))

    start_rect = text.text_start.get_rect()
    start_box = Box(white, 200, 100, (3*grid_width, 7.2*grid_height))
    start_rect.center = (start_box.center)

    quit_rect = text.text_quit.get_rect()
    quit_box = Box(white, 200, 100, (5*grid_width, 7.2*grid_height))
    quit_rect.center = (quit_box.center)

# Set the variables for user choises. We pass these as attributes to the next (game) screen.
    computer1_level = 1
    computer2_level = 1
    paddle1_color = yellow
    paddle2_color = green
    player1_is_computer = False
    player2_is_computer = False

    text_comp_level1 = smallfont.render(str(computer1_level), True, red)
    text_comp_level2 = smallfont.render(str(computer2_level), True, red)

    comp_level1_rect = text_comp_level1.get_rect()
    comp_level1_rect.center = (2*grid_width, 4*grid_height)

    comp_level2_rect = text_comp_level2.get_rect()
    comp_level2_rect.center = (6*grid_width, 4*grid_height)

# Make a while loop for the start screen. The screen updates at 15hz.
    intro = True

    while intro:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                exit()

# Make selections with mouse button click.
            if e.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_position = (e.pos[0], e.pos[1])
                # We define the is_inside unction in the functions.py file. It checks if the first parameter is inside the second. This is how we write the selections in the variables that were introduced before
                if is_inside(mouse_position, human1_box):
                    player1_is_computer = False
                if is_inside(mouse_position, human2_box):
                    player2_is_computer = False

                if is_inside(mouse_position, computer1_box):
                    player1_is_computer = True
                if is_inside(mouse_position, computer2_box):
                    player2_is_computer = True

                if is_inside(mouse_position, minus1_box) and computer1_level > 1:
                    computer1_level -= 1
                if is_inside(mouse_position, plus1_box) and computer1_level < 10:
                    computer1_level += 1
                if is_inside(mouse_position, minus2_box) and computer2_level > 1:
                    computer2_level -= 1
                if is_inside(mouse_position, plus2_box) and computer2_level < 10:
                    computer2_level += 1

                if is_inside(mouse_position, paddle1_box_yellow):
                    paddle1_color = yellow
                if is_inside(mouse_position, paddle1_box_green):
                    paddle1_color = green
                if is_inside(mouse_position, paddle1_box_red):
                    paddle1_color = red
                if is_inside(mouse_position, paddle1_box_blue):
                    paddle1_color = blue

                if is_inside(mouse_position, paddle2_box_yellow):
                    paddle2_color = yellow
                if is_inside(mouse_position, paddle2_box_green):
                    paddle2_color = green
                if is_inside(mouse_position, paddle2_box_red):
                    paddle2_color = red
                if is_inside(mouse_position, paddle2_box_blue):
                    paddle2_color = blue

# When the start button is pressed we break out  of the while loop.
                if is_inside(mouse_position, start_box):
                    intro = False
                if is_inside(mouse_position, quit_box):
                    exit()

# Fill the screen with black and draw the boxes and text on the screen.
        screen.fill(black)
        human1_box.show()
        screen.blit(text.text_player1, player1_rect)
        screen.blit(text.text_player2, player2_rect)

        screen.blit(text.text_human, human1_rect)
        computer1_box.show()
        screen.blit(text.text_computer, computer1_rect)
        human2_box.show()
        screen.blit(text.text_human, human2_rect)
        computer2_box.show()
        screen.blit(text.text_computer, computer2_rect)

# Only show the computer difficulty level if the computer is chosen as another player
        if player1_is_computer == True:
            text_comp_level1 = smallfont.render(
                str(computer1_level), True, red)

            screen.blit(text.text_level, level1_rect)
            screen.blit(text_comp_level1, comp_level1_rect)
            minus1_box.show()
            screen.blit(text.text_minus, minus1_rect)
            plus1_box.show()
            screen.blit(text.text_plus, plus1_rect)
        if player2_is_computer == True:
            text_comp_level2 = smallfont.render(
                str(computer2_level), True, red)

            screen.blit(text.text_level, level2_rect)
            screen.blit(text_comp_level2, comp_level2_rect)
            plus2_box.show()
            screen.blit(text.text_plus, plus2_rect)
            minus2_box.show()
            screen.blit(text.text_minus, minus2_rect)

        screen.blit(text.text_paddle_color, paddle_color1_rect)
        screen.blit(text.text_paddle_color, paddle_color2_rect)

        paddle1_box_yellow.show()
        paddle1_box_green.show()
        paddle1_box_red.show()
        paddle1_box_blue.show()

        paddle2_box_yellow.show()
        paddle2_box_green.show()
        paddle2_box_red.show()
        paddle2_box_blue.show()

# Draw an X on the chosen paddle colors
        if paddle1_color == yellow:
            screen.blit(
                text.text_x, paddle1_box_yellow.center)
        if paddle1_color == green:
            screen.blit(
                text.text_x, paddle1_box_green.center)
        if paddle1_color == red:
            screen.blit(
                text.text_x, paddle1_box_red.center)
        if paddle1_color == blue:
            screen.blit(
                text.text_x, paddle1_box_blue.center)

        if paddle2_color == yellow:
            screen.blit(
                text.text_x, paddle2_box_yellow.center)
        if paddle2_color == green:
            screen.blit(
                text.text_x, paddle2_box_green.center)
        if paddle2_color == red:
            screen.blit(
                text.text_x, paddle2_box_red.center)
        if paddle2_color == blue:
            screen.blit(
                text.text_x, paddle2_box_blue.center)

        start_box.show()
        screen.blit(text.text_start, start_rect)
        quit_box.show()
        screen.blit(text.text_quit, quit_rect)

        pygame.display.flip()

        # We choose 15hz as refresh rate. This is because there are no moving objects and it doesn't need to be faster.
        clock.tick(15)
# After the while loop we move to the game screen (we run the function and pass the necessary information as parameters.)
    show_mygame(player1_is_computer, player2_is_computer,
                computer1_level, computer2_level, paddle1_color, paddle2_color)
