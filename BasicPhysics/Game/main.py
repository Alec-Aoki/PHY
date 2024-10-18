import random
import pygame
#Initializing pygame
pygame.init()

    ### SCREEN ###
XAXIS = 800
YAXIS = 600
#Creating screen                   X    Y
screen = pygame.display.set_mode((XAXIS, YAXIS))

#Setting background colour
screen.fill((0,0,0)) #RGB, max = 255, 255, 255 = white
pygame.display.update()

#Setting title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

DEFAULT_IMAGE_SIZE = (64,64)
    ### END OF SCREEN ###

    ### PLAYER ###
#Player Image
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE)

#Player Function
def player(playerX, playerY):
    #"Drawing" the player
    screen.blit(playerImg,(playerX, playerY))

playerX = XAXIS/2
playerY = YAXIS/2 + 150
playerXChange = 0
playerYChange = 0
    ### END OF PLAYER ###

    ### ENEMY ###
#Enemy Image
enemyImg = pygame.image.load('enemy.png')
enemyImg = pygame.transform.scale(enemyImg, DEFAULT_IMAGE_SIZE)

#Enemy Function
def enemy(enemyX, enemyY):
    screen.blit(enemyImg,(enemyX, enemyY))

#Randomize enemy spawn position
enemyX = random.randint(0, XAXIS-64)
enemyY = random.randint(0, (int)(YAXIS/4))
enemyXChange = 0
enemyYChange = 0
    ### END OF ENEMY ###

    ### GAME LOOP ###
running = True

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            running = False

        #Movement Input
        if event.type == pygame.KEYDOWN: #Checks if a key has been pressed
            if event.key == pygame.K_LEFT:
                playerXChange = -0.3
            if event.key == pygame.K_RIGHT:
                playerXChange = 0.3
            if event.key == pygame.K_DOWN:
                playerYChange = 0.3
            if event.key == pygame.K_UP:
                playerYChange = -0.3

        if event.type == pygame.KEYUP: #Checks if a key has been released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXChange = 0
            if event.key == pygame.K_UP or pygame.key == pygame.K_DOWN:
                playerYChange = 0

        #Enemy "AI"
        if playerX <= enemyX:
            if enemyX < XAXIS/2 and enemyX > 0:
                enemyXChange = 0.1
        else:
            enemyXChange = -0.1
        
        enemyYChange = 0.1

    playerX += playerXChange
    playerY += playerYChange

    enemyX += enemyXChange
    enemyY += enemyYChange

    #Borders
    if playerX <= 0:
        playerX = 0
    elif playerX >= XAXIS-64:
        playerX = XAXIS-64
    if playerY <= 0:
        playerY = 0
    elif playerY >= YAXIS-64:
        playerY = YAXIS-64
    if enemyX <= 0:
        enemyX = 0
    elif enemyX >= XAXIS-64:
        enemyX = XAXIS-64

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
    ### END OF GAME LOOP ###