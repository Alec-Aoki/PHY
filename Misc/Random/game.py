import pygame
pygame.init() #initializing pygame library

screen_width = 500
screen_height = 500

#creating game window (500x500)
win = pygame.display.set_mode((screen_width, screen_height))

#caption of the window
pygame.display.set_caption("First Game")

#main character atributes
x = 50
y = 425
width = 40
height = 60
vel = 5

#jumping
isJump = False
jumpCount = 10

##### main loop #####
run = True
while (run):
    pygame.time.delay(25) #in milliseconds

    #checking for events
    for event in pygame.event.get():
        #close the game
        if (event.type == pygame.QUIT):
            run = False

    #move character, stop at borders
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] and x > vel):
        x -= vel

    if (keys[pygame.K_RIGHT] and x < (screen_width - width - vel)):
        x += vel
    if (not(isJump)):
        #not jumping, can move up or down
        #if (keys[pygame.K_UP] and y > vel):
        #    y -= vel
        #
        #if (keys[pygame.K_DOWN] and y < (screen_height - height - vel)):
        #    y += vel
        if (keys[pygame.K_SPACE]):
            isJump = True
    else:
        #jumping, cant move up or down
        if (jumpCount >= -10):
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2)*0.5*neg #parable behavior, switches signal after half (starts going down)
            jumpCount -= 1
        else:
            #jump finished, reset jump parameters
            isJump = False
            jumpCount = 10

    #fills the screen every clock so we dont constantly draw the character
    win.fill((0, 0, 0))

    #drawing the character
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
                    #window  RGB        character atributes
    pygame.display.update()
pygame.quit()