import pygame as pg

pg.init() 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.7)

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Shooter')

bgImg = pg.image.load('Savanna.png')

run = True
while run:
    screen.blit(bgImg, (0, 0))

    for event in pg.event.get():
        # quit game
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
pg.quit()
