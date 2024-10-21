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
enemyX = random.randint(250, XAXIS-250)
enemyY = random.randint(0, (int)(YAXIS/5))
enemyXChange = 0
enemyYChange = 0
    ### END OF ENEMY ###

    ### BORDER ###
def checkBorder(objectX, objectY):
    if objectX <= 0:
        objectX = 0
    elif objectX >= XAXIS - 64:
        objectX = XAXIS-64
    
    if objectY <= 0:
        objectY = 0
    elif objectY >= YAXIS - 64:
        objectY = YAXIS - 64

    return objectX, objectY
    ### END OF BORDER ###

    ### INPUT ###
def movementInput(event, objectX, objectY):
    #Movement Input
    if event.type == pygame.KEYDOWN: #Checks if a key has been pressed
        if event.key == pygame.K_LEFT:
            objectX = -0.5
        if event.key == pygame.K_RIGHT:
            objectX = 0.5
        if event.key == pygame.K_DOWN:
            objectY = 0.5
        if event.key == pygame.K_UP:
            objectY = -0.5

    if event.type == pygame.KEYUP: #Checks if a key has been released
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            objectX = 0
        if event.key == pygame.K_UP or pygame.key == pygame.K_DOWN:
            objectY = 0

    return objectX, objectY
    ### END OF INPUT ###

    ### GAME LOOP ###
running = True

while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT:
            running = False

        #Movement input
        playerXChange, playerYChange = movementInput(event, playerXChange, playerYChange)

        #Enemy "AI"
        if playerX <= enemyX:
            if enemyX > XAXIS-200:
                enemyXChange = -0.2
            else:
                enemyXChange = 0.2
        elif playerX > enemyX:
            if enemyX < 200:
                enemyXChange = 0.2
            else:
                enemyXChange = -0.2
        
        enemyYChange = 0.1

    playerX += playerXChange
    playerY += playerYChange

    enemyX += enemyXChange
    enemyY += enemyYChange

    #Borders
    playerX, playerY = checkBorder(playerX, playerY)
    enemyX, _ = checkBorder(enemyX, enemyY)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
    ### END OF GAME LOOP ###