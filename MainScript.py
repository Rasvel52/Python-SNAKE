from random import randrange
class Sett():
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
