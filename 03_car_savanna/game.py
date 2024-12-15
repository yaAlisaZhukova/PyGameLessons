import pygame as pg

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.7)

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Shooter')

carX = 200
carY = 240
carImg = pg.image.load('blueCarSmall.png')
bgImg = pg.image.load('Savanna.png')

def keyPressed():
    global carX, carY

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        carX -= 0.5
    if keys[pg.K_RIGHT]:
        carX += 0.5
    if keys[pg.K_UP]:
        carY -= 1
    if keys[pg.K_DOWN]:
        carY += 0.5

run = True
while run:
    screen.blit(bgImg, (0, 0))
    screen.blit(carImg, (carX, carY))
    keyPressed()

    if carY > SCREEN_HEIGHT:
        carY = 240
    carY += 0.5

    for event in pg.event.get():
        # quit game
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
pg.quit()
