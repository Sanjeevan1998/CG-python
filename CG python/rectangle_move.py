
import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
UN = (94,23,12)
pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bounce Rectangle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------

#Starting postion of the rectangle
rect_x=430.1165
rect_y=430.1165
p1=0
p2=0
#Original Size of the rectangles
rect_a=50
rect_b=30

#Speed direction of the rectangle
rect_change_x=5#random.randrange(1,10)
rect_change_y=5#random.randrange(1,10)
rect_change_size_x=0
rect_change_size_y=0
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # --- Drawing code
    pygame.draw.rect(screen,WHITE,[rect_x,rect_y,rect_change_size_x+rect_a,rect_change_size_x+rect_a])
    pygame.draw.rect(screen,GREEN,[rect_x+10,rect_y+10,rect_change_size_y+rect_b,rect_change_size_y+rect_b])
    pygame.draw.rect(screen,RED,[rect_x+50,rect_y+50,rect_change_size_x+rect_a,rect_change_size_x+rect_a])
    pygame.draw.rect(screen,UN,[rect_x+60,rect_y+60,rect_change_size_y+rect_b,rect_change_size_y+rect_b])
    rect_x+=rect_change_x
    rect_y+=rect_change_y
    if rect_x>650 or rect_x<0:
        rect_change_x=rect_change_x*-1
    elif rect_y>450 or rect_y<0:
        rect_change_y=rect_change_y*-1
    if rect_change_size_x+rect_a>100:
        p1=1
    elif rect_change_size_x+rect_a<0:
        p1=0
    if rect_change_size_y+rect_b>80 or rect_change_size_y+rect_b<0:
        p2=1
    elif rect_change_size_x+rect_b<0:
        p2=0
    if p1==0 or p2==0:
        rect_change_size_x+=1
        rect_change_size_y+=1
    elif p1==1 and p2==1:
        rect_change_size_x-=1
        rect_change_size_y-=1

    # --- Go ahead and update the screen with what we've drawn.
    #time.sleep(0.1)
    pygame.display.flip()

    # --- Limit to 60 frames per second

    clock.tick(60)

# Close the window and quit.

pygame.quit()
