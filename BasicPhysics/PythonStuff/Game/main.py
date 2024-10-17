import pygame
#Initializing pygame
pygame.init()

    ### Screen ###
#Creating screen
screen = pygame.display.set_mode((800, 600))

#Setting background colour
screen.fill((255,255,255)) #RGB, max = 255, 255, 255 = black
pygame.display.update()

#Setting title and icon
pygame.display.set_caption('The Suspicious Game')
icon = pygame.image.load('sus.png')
pygame.display.set_icon(icon)

    ### Game Loop ###
running = True
while(running):
    for event in pygame.event.get():
        #Quit window event
        if event.type == pygame.QUIT:
            running = False