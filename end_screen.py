# We bring the winner as parameter from the game screen/function.
def show_end_screen(player2_won, player1_won):
    from functions import is_inside
    import pygame
    from constants import screen_width, screen_height, black, grid_height, grid_width, white
    import text
    from classes import Box
    from start_screen import show_start_screen

# Let's again fill the screen and initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(black)

    pygame.display.set_caption("Pong by Ville")
    clock = pygame.time.Clock()

# We also need some text drawn on the screen. And we get the text positions here too.
    player1_rect = text.text_player1.get_rect()
    player1_rect.center = (4*grid_width, 3*grid_height)

    player2_rect = text.text_player2.get_rect()
    player2_rect.center = (4*grid_width, 3*grid_height)

    won_rect = text.text_won.get_rect()
    won_rect.center = (4*grid_width, 4*grid_height)

    play_again_rect = text.text_play_again.get_rect()
    play_again_rect.center = (4*grid_width, 6*grid_height)

    start_rect = text.text_start.get_rect()
    start_box = Box(white, 200, 100, (3*grid_width, 7.2*grid_height))
    start_rect.center = (start_box.center)

    quit_rect = text.text_quit.get_rect()
    quit_box = Box(white, 200, 100, (5*grid_width, 7.2*grid_height))
    quit_rect.center = (quit_box.center)

# And we again make a while loop to show the end screen
    outro = True

    while outro:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                exit()

# Check the mouse button presses and euther quit or start a new game
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = (e.pos[0], e.pos[1])

# If start again screen is pressed we break the loop. NOTE the button needs two presses and I'm not sure why?
                if is_inside(mouse_position, start_box):
                    outro = False
                if is_inside(mouse_position, quit_box):
                    exit()

# Fill the screen with black
        screen.fill(black)

# Check the winner and set the text accordingly
        if player1_won:
            screen.blit(text.text_player1, player1_rect)
        if player2_won:
            screen.blit(text.text_player2, player2_rect)

        screen.blit(text.text_won, won_rect)
        screen.blit(text.text_play_again, play_again_rect)

        start_box.show()
        screen.blit(text.text_start, start_rect)
        quit_box.show()
        screen.blit(text.text_quit, quit_rect)

        pygame.display.flip()

        # Refresh rate is set at 15hz
        clock.tick(15)

    # Go back to the start screen if while loop is broken
    show_start_screen()
