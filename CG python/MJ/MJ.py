import pygame
import time

pygame.init()


display_width = 1368
display_height = 768

mjlist=['mj1.jpg','mj2.jpg','mj3.jpg','mj4.jpg','mj5.jpg','mj6.jpg','mj7.jpg','mj8.jpg','mj9.jpg','mj10.jpg']
mjrevlist=['mj1-ConvertImage.jpg','mj2-ConvertImage.jpg','mj3-ConvertImage.jpg','mj4-ConvertImage.jpg','mj5-ConvertImage.jpg','mj6-ConvertImage.jpg','mj7-ConvertImage.jpg','mj8-ConvertImage.jpg','mj9-ConvertImage.jpg','mj10-ConvertImage.jpg']

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MJ')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

w1=0

x = 0
y = 250
xchange = 5

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    mjImg = pygame.image.load(mjlist[w1])
    mjImgrev = pygame.image.load(mjrevlist[w1])
    gameDisplay.fill(white)
    pygame.display.flip()
    #pygame.draw.circle(gameDisplay,white,[x+130,y+50],250)
    if(xchange==5):
        gameDisplay.blit(mjImg,(x,y))

    elif(xchange==-5):
        gameDisplay.blit(mjImgrev,(x,y))

    pygame.display.flip()
    x+=xchange
    w1+=1

    if(x>1200 or x<0):
        xchange=xchange*-1

    if(w1>9):
        w1=0
        pygame.display.flip()

    else:
        pass
        pygame.display.flip()

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
quit()
