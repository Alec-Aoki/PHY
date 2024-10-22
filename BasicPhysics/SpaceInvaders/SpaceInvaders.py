import random
import math
import pygame



#Initializing pygame
pygame.init()



    ### SCREEN ###
XAXIS = 800
YAXIS = 600

screen = pygame.display.set_mode((XAXIS, YAXIS)) #Creating screen

screen.fill((0,0,0)) #Setting background, RGB, max = 255, 255, 255 = white
pygame.display.update()

pygame.display.set_caption('Space Invaders') #Setting title and icon
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

DEFAULT_IMAGE_SIZE = (64,64)
    ### END OF SCREEN ###




    ### PLAYER ###
playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE)

def player(playerX, playerY):
    screen.blit(playerImg,(playerX, playerY)) #Drawing the player

playerX = XAXIS/2
playerY = YAXIS/2 + 150
playerXChange = 0
playerYChange = 0
playerScore = 0
    ### END OF PLAYER ###




    ### ENEMY ###
enemyImg = pygame.image.load('enemy.png')
enemyImg = pygame.transform.scale(enemyImg, DEFAULT_IMAGE_SIZE)

def enemy(enemyX, enemyY):
    screen.blit(enemyImg,(enemyX, enemyY))

def enemyMov(playerXmov, enemyXmov):
    if playerXmov <= enemyXmov:
        if enemyXmov > XAXIS-200:
            enemyXChangemov = -0.1
        else:
            enemyXChangemov = 0.1
    elif playerXmov > enemyXmov:
        if enemyXmov < 200:
            enemyXChangemov = 0.1
        else:
            enemyXChangemov = -0.1
        
    enemyYChangemov = 0.05

    return enemyXChangemov, enemyYChangemov

enemyX = random.randint(250, XAXIS-250) #Randomize enemy spawn position
enemyY = 16
enemyXChange = 0
enemyYChange = 0
    ### END OF ENEMY ###





    ### LASER ###
laserImg = pygame.image.load('laser.png')
laserX = playerX
laserY = playerY
laserYChange = -0.75
laserState = 'ready'
def fireLaser(laserX, laserY):
    global laserState
    laserState = 'firing'
    screen.blit(laserImg,(laserX, laserY))
    ### END OF LASER ###




    ### COLLISION ###
def hasCollided(object1X, object1Y, object2X, object2Y):
    distance = math.sqrt((math.pow(object2X - object1X, 2)) + (math.pow(object2Y - object1Y, 2)))
    if distance < 27:
        return True
    else:
        return False
    ### END OF COLLISION ###




    ### BORDER ###
def checkBorder(objectX, objectY, object):
    if object == 'player' or object == 'enemy':
        if objectX <= 0:
            objectX = 0
        elif objectX >= XAXIS - 64:
            objectX = XAXIS-64
        
        if objectY <= 0:
            objectY = 0
        elif objectY >= YAXIS - 64:
            objectY = YAXIS - 64
    elif object == 'laser':
        if objectY <= 0:
            objectX = playerX
            objectY = playerY
            global laserState
            laserState = 'ready'

    return objectX, objectY
    ### END OF BORDER ###




    ### INPUT ###
def movementInput(event, objectX, objectY):
    if event.type == pygame.KEYDOWN: #Checks if a key has been pressed
        if event.key == pygame.K_LEFT:
            objectX = -0.5
        if event.key == pygame.K_RIGHT:
            objectX = 0.5
        if event.key == pygame.K_DOWN:
            objectY = 0.5
        if event.key == pygame.K_UP:
            objectY = -0.5
        if event.key == pygame.K_SPACE:
            fireLaser(laserX, laserY)

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
        if event.type == pygame.QUIT:
            running = False

        playerXChange, playerYChange = movementInput(event, playerXChange, playerYChange)

        enemyXChange, enemyYChange = enemyMov(playerX, enemyX)

    if laserState == 'firing':
        fireLaser(laserX, laserY)
        laserY += laserYChange

    playerX += playerXChange
    playerY += playerYChange
    enemyX += enemyXChange
    enemyY += enemyYChange

    playerX, playerY = checkBorder(playerX, playerY, 'player')
    enemyX, _ = checkBorder(enemyX, enemyY, 'enemy')
    laserX, laserY = checkBorder(laserX, laserY, 'laser')

    if hasCollided(enemyX, enemyY, laserX, laserY):
        enemyX = random.randint(250, XAXIS-250)
        enemyY = 16
        laserX, laserY = checkBorder(laserX, 0, 'laser')
        laserState = 'ready'
        playerScore += 1
        print(playerScore)

    player(playerX, playerY) #Update objects
    enemy(enemyX, enemyY)

    pygame.display.update()
    ### END OF GAME LOOP ###