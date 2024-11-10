import pygame
import time
import random

# Constants
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
SNAKE_SPEED = 10
BLOCK_SIZE = 10

# Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 0)

def init_game():
    """Initialize game state and pygame"""
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    
    game_state = {
        'snake_position': [100, 50],
        'snake_body': [[100, 50], [90, 50], [80, 50], [70, 50]],
        'food_position': generate_food_position(),
        'direction': 'RIGHT',
        'change_to': 'RIGHT',
        'score': 0,
        'running': True
    }
    
    return window, clock, game_state

def generate_food_position():
    """Generate new random position for food"""
    return [
        random.randrange(1, (WINDOW_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
        random.randrange(1, (WINDOW_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
    ]

def handle_input(game_state):
    """Handle keyboard input and window events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state['running'] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game_state['change_to'] = 'UP'
            elif event.key == pygame.K_DOWN:
                game_state['change_to'] = 'DOWN'
            elif event.key == pygame.K_LEFT:
                game_state['change_to'] = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                game_state['change_to'] = 'RIGHT'

def update_direction(game_state):
    """Update snake direction based on input"""
    direction_pairs = {
        'UP': 'DOWN',
        'DOWN': 'UP',
        'LEFT': 'RIGHT',
        'RIGHT': 'LEFT'
    }
    
    change_to = game_state['change_to']
    if change_to != direction_pairs.get(game_state['direction']):
        game_state['direction'] = change_to

def update_snake_position(game_state):
    """Update snake position based on current direction"""
    movement = {
        'UP': (0, -BLOCK_SIZE),
        'DOWN': (0, BLOCK_SIZE),
        'LEFT': (-BLOCK_SIZE, 0),
        'RIGHT': (BLOCK_SIZE, 0)
    }
    
    dx, dy = movement[game_state['direction']]
    game_state['snake_position'][0] += dx
    game_state['snake_position'][1] += dy

def check_collisions(game_state):
    """Check for collisions with walls and snake body"""
    pos = game_state['snake_position']
    
    # Wall collisions
    if (pos[0] < 0 or pos[0] > WINDOW_WIDTH - BLOCK_SIZE or
        pos[1] < 0 or pos[1] > WINDOW_HEIGHT - BLOCK_SIZE):
        return True
        
    # Self collision
    if pos in game_state['snake_body'][1:]:
        return True
        
    return False

def update_snake_body(game_state):
    """Update snake body and handle food collision"""
    game_state['snake_body'].insert(0, list(game_state['snake_position']))
    
    # Check if snake ate food
    if (game_state['snake_position'][0] == game_state['food_position'][0] and
        game_state['snake_position'][1] == game_state['food_position'][1]):
        game_state['score'] += 10
        game_state['food_position'] = generate_food_position()
    else:
        game_state['snake_body'].pop()

def draw_game(window, game_state):
    """Draw the current game state"""
    window.fill(BLACK)
    
    # Draw snake
    for pos in game_state['snake_body']:
        pygame.draw.rect(window, GREEN,
                        pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    
    # Draw food
    pygame.draw.rect(window, WHITE,
                    pygame.Rect(game_state['food_position'][0],
                              game_state['food_position'][1],
                              BLOCK_SIZE, BLOCK_SIZE))
    
    # Draw score
    show_score(window, game_state['score'])
    pygame.display.update()

def show_score(window, score):
    """Display current score"""
    font = pygame.font.SysFont('times new roman', 20)
    score_surface = font.render(f'Score: {score}', True, WHITE)
    score_rect = score_surface.get_rect()
    window.blit(score_surface, score_rect)

def show_game_over(window, score):
    """Display game over screen"""
    font = pygame.font.SysFont('times new roman', 50)
    surface = font.render(f'Your Score is: {score}', True, RED)
    rect = surface.get_rect()
    rect.midtop = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4)
    window.blit(surface, rect)
    pygame.display.flip()
    time.sleep(2)

def main():
    """Main game loop"""
    window, clock, game_state = init_game()
    
    while game_state['running']:
        handle_input(game_state)
        update_direction(game_state)
        update_snake_position(game_state)
        
        if check_collisions(game_state):
            show_game_over(window, game_state['score'])
            break
            
        update_snake_body(game_state)
        draw_game(window, game_state)
        clock.tick(SNAKE_SPEED)
    
    pygame.quit()

if __name__ == "__main__":
    main()