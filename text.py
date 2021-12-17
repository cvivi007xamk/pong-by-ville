from constants import white
import pygame
pygame.init()

# Here we define some text that is used in the app. Again this is separated for easier maintainability and imports and reuse. Also the used fonts are defined here.

smallfont = pygame.font.SysFont('times', 30)
largefont = pygame.font.SysFont('times', 40)

text_intro = smallfont.render('Make your choices.', True, white)
text_player1 = smallfont.render('Player 1', True, white)
text_player2 = smallfont.render('Player 2', True, white)
text_human = smallfont.render('Human', True, white)
text_computer = smallfont.render('Computer', True, white)
text_level = smallfont.render('Computer level', True, white)
text_plus = smallfont.render('+', True, white)
text_minus = smallfont.render('-', True, white)
text_paddle_color = smallfont.render('Choose paddle color', True, white)
text_x = largefont.render('X', True, white)
text_start = smallfont.render('START', True, white)
text_quit = smallfont.render('QUIT', True, white)
text_play_again = smallfont.render('Play again?', True, white)
text_won = largefont.render('WON', True, white)
