import pygame
import math
import random

print("Condicoes iniciais aleatorias? (S/N)")
resposta = input()
if resposta == 'S':
    condIniAleat = True
else:
    condIniAleat = False

#Constantes
G = 6.67430
if condIniAleat:
    MASSA_ESTRELA = random.randint(300000, 400000)
else:
    print("Digite a massa da estrela: ")
    MASSA_ESTRELA = float(input())
#RAIO_ESTRELA = pow(MASSA_ESTRELA, (1.0 / 3.0)) #Raio proporcional à massa
RAIO_ESTRELA = 17
EIXOX = 1300
EIXOY = 700

#Classe PLANETA
class PLANETA:
    def __init__(planeta):
        if condIniAleat:
            planeta.massa = random.randint(1, 2)
            planeta.raio = 7.5
            #planeta.raio = pow(planeta.massa, (1.0 / 3.0))
            planeta.x = random.uniform(-500, -100)
            planeta.y = random.uniform(-500, -100)
            planeta.vx = random.uniform(0, 100)
            planeta.vy = 0
            planeta.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            planeta.ativo = True

        else:
            print("Massa do planeta: ")
            planeta.massa = float(input())
            planeta.raio = 7.5
            #planeta.raio = pow(planeta.massa, (1.0 / 3.0))
            print("Posição inicial no eixo x: ")
            planeta.x = float(input())
            print("Posicao inicial no eixo y: ")
            planeta.y = float(input())
            print("Velocidade inicial no eixo x: ")
            planeta.vx = float(input())
            print("Velocidade inical no eixo y: ")
            planeta.vy = float(input())
            planeta.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            planeta.ativo = True

    def calcularGravidade(planeta):
        dx = -planeta.x
        dy = -planeta.y
        distancia = math.sqrt(pow(dx, 2) + pow(dy, 2))

        if distancia == 0:
            return
        
        forcaGravitacional = G * MASSA_ESTRELA * planeta.massa / (pow(distancia, 2))

        ax = forcaGravitacional * dx / (distancia * planeta.massa)
        ay = forcaGravitacional * dy / (distancia * planeta.massa)

        planeta.vx += ax
        planeta.vy += ay

    def atualizarPosicao(planeta):
        if planeta.ativo:
            planeta.calcularGravidade()
            planeta.x += planeta.vx
            planeta.y += planeta.vy

def desenharSprite(tela, cor, cx, cy, raio):
    pygame.draw.circle(tela, cor, (int(cx + EIXOX / 2), int(cy + EIXOY / 2)), int(raio))

def simular():
    pygame.init()
    tela = pygame.display.set_mode((EIXOX, EIXOY))
    clock = pygame.time.Clock()

    print("Quantidade de planetas: ")
    quantPlanetas = int(input())

    planetas = [PLANETA() for _ in range(quantPlanetas)]

    simulando = True
    while simulando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                simulando = False

        tela.fill((0, 0, 0))

        desenharSprite(tela, (255, 0, 0), 0, 0, RAIO_ESTRELA)

        for planeta in planetas:
            planeta.atualizarPosicao()
            desenharSprite(tela, planeta.cor, planeta.x, planeta.y, planeta.raio)

        pygame.display.flip()
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    simular()