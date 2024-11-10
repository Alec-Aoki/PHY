import pygame
import time
import random

"""
Alterações
1. Simplificar documentação de funções
2. Remover comentários desnecessários/repetitivos
3. Adicionar sair do jogo quando a tela é fechada

Para tornar o código mais claro, poderíamos usar POO/modularizar em múltiplas funções, mas achei muito avançado.
"""

def show_score(color, font, size):
    """
    Esta função usa a variável global `score`, que deve ser definida em outro ponto do código.
    Parâmetros:
        color (tuple): Uma tupla RGB que define a cor do texto (ex: (255, 255, 255) para branco).
        font (str): O nome da fonte que será usada para exibir o texto da pontuação (ex: 'Arial', 'Comic Sans MS').
        size (int): O tamanho da fonte a ser usada para o texto da pontuação.
    """
    score_font = pygame.font.SysFont(font, size)
    
    # Cria a superfície do texto que exibe a pontuação
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # Obtém o retângulo para posicionar o texto na tela
    score_rect = score_surface.get_rect()
    
    game_window.blit(score_surface, score_rect)


def game_over():
    """
    Exibe a tela de fim de jogo com a pontuação final e encerra o programa.
    Variáveis Globais Utilizadas:
        score (int): A pontuação final do jogador, que será exibida no texto de fim de jogo.
        window_x (int): A largura da janela do jogo, usada para centralizar o texto horizontalmente.
        window_y (int): A altura da janela do jogo, usada para definir a posição do texto na parte superior central da tela.
        red (tuple): Uma tupla RGB que define a cor vermelha usada para o texto (ex: (255, 0, 0)).
        game_window (pygame.Surface): A superfície da janela do jogo onde o texto de fim de jogo será exibido.
    """
    my_font = pygame.font.SysFont('times new roman', 50)
    
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    
    game_over_rect = game_over_surface.get_rect()
    
    # Define a posição do texto para o centro superior da tela
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    time.sleep(2)
    
    # Encerra o PyGame e o programa
    pygame.quit()
    quit()


#Constantes
snake_speed = 10

window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

pygame.init()

pygame.display.set_caption('Jogo da cobrinha')
game_window = pygame.display.set_mode((window_x, window_y))

# Define a taxa de atualização do jogo
fps = pygame.time.Clock()

# Valores Iniciais

snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# Direção inicial para a qual a cobra vai andar 
direction = 'RIGHT'
change_to = direction

score = 0

running = True

# Main Function
while running:
    # Lidando com eventos de teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Fecha o jogo quando a janela é fechada
            running = False
        if event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Evita que a cobra se mova em duas direções simultaneamente e também impede que ela se mova diretamente na direção oposta
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Movendo a cobra com base na direção atual
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # A cobra anda a partir de um mecanismo no qual acrescentamos uma posição na cabeça e removemos uma posição ao final: 
    # Mecanismo de crescimento do corpo da cobra: se a cobra colidir com a fruta, a pontuação será incrementada em 10 pontos
    snake_body.insert(0, list(snake_position))  # Adiciona a nova posição da cabeça da cobra ao corpo
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10 
        fruit_spawn = False  # Indica que uma nova fruta precisa ser gerada
    else:
        snake_body.pop()  # Remove a última posição da cobra se não houver colisão com a fruta

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                          random.randrange(1, (window_y // 10)) * 10]
        
    fruit_spawn = True

    game_window.fill(black)

    # Desenha cada segmento do corpo da cobra na tela
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))


    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Colisão com o próprio corpo da cobra
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(snake_speed)  # Controla a velocidade do jogo com base na variável `snake_speed`

