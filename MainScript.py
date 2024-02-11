from random import randrange
import pygame
class Sett():
    pygame.init()
    Res = 800
    Size = 50
    x, y = randrange(0, Res, Size), randrange(0, Res, Size)
    apple = randrange(0, Res, Size), randrange(0, Res, Size)
    length = 1
    snake = [(x, y)]
    dirx, diry = 0, Size
    fps = 10
    bg_color = (0, 0, 0)
    x += dirx * Size
    y += diry * Size
    Control = {'W':True, 'S':True, 'A':True, 'D':True}
    Font_Score = pygame.font.Font(None, 36)
    Font_End = pygame.font.Font(None, 110)
    score = 0
    New_Score = 10
