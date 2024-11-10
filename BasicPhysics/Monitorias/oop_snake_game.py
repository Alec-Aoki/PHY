import pygame
import time
import random

class Colors:
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREEN = pygame.Color(0, 255, 0)
    BLUE = pygame.Color(0, 0, 255)

class Config:
    WINDOW_WIDTH = 720
    WINDOW_HEIGHT = 480
    SNAKE_SPEED = 10
    BLOCK_SIZE = 10
    
class Snake:
    def __init__(self, start_pos):
        self.position = list(start_pos)
        self.body = [
            list(start_pos),
            [start_pos[0] - 10, start_pos[1]],
            [start_pos[0] - 20, start_pos[1]],
            [start_pos[0] - 30, start_pos[1]]
        ]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def update(self):
        # Update direction based on input
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # Move snake
        if self.direction == 'UP':
            self.position[1] -= Config.BLOCK_SIZE
        if self.direction == 'DOWN':
            self.position[1] += Config.BLOCK_SIZE
        if self.direction == 'LEFT':
            self.position[0] -= Config.BLOCK_SIZE
        if self.direction == 'RIGHT':
            self.position[0] += Config.BLOCK_SIZE

    def grow(self):
        self.body.insert(0, list(self.position))
        
    def move(self):
        self.body.insert(0, list(self.position))
        self.body.pop()

    def check_collision(self):
        # Wall collision
        if (self.position[0] < 0 or 
            self.position[0] > Config.WINDOW_WIDTH - Config.BLOCK_SIZE or
            self.position[1] < 0 or 
            self.position[1] > Config.WINDOW_HEIGHT - Config.BLOCK_SIZE):
            return True
            
        # Self collision
        for block in self.body[1:]:
            if self.position[0] == block[0] and self.position[1] == block[1]:
                return True
        return False

class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return [
            random.randrange(1, (Config.WINDOW_WIDTH // Config.BLOCK_SIZE)) * Config.BLOCK_SIZE,
            random.randrange(1, (Config.WINDOW_HEIGHT // Config.BLOCK_SIZE)) * Config.BLOCK_SIZE
        ]

    def spawn_new(self):
        self.position = self.generate_position()

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake = Snake([100, 50])
        self.food = Food()
        self.score = 0
        self.running = True

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    self.snake.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    self.snake.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_to = 'RIGHT'

    def show_score(self):
        font = pygame.font.SysFont('times new roman', 20)
        surface = font.render(f'Score: {self.score}', True, Colors.WHITE)
        rect = surface.get_rect()
        self.window.blit(surface, rect)

    def show_game_over(self):
        font = pygame.font.SysFont('times new roman', 50)
        surface = font.render(f'Your Score is: {self.score}', True, Colors.RED)
        rect = surface.get_rect()
        rect.midtop = (Config.WINDOW_WIDTH / 2, Config.WINDOW_HEIGHT / 4)
        self.window.blit(surface, rect)
        pygame.display.flip()
        time.sleep(2)

    def draw(self):
        self.window.fill(Colors.BLACK)
        
        # Draw snake
        for pos in self.snake.body:
            pygame.draw.rect(
                self.window, 
                Colors.GREEN,
                pygame.Rect(pos[0], pos[1], Config.BLOCK_SIZE, Config.BLOCK_SIZE)
            )
        
        # Draw food
        pygame.draw.rect(
            self.window,
            Colors.WHITE,
            pygame.Rect(
                self.food.position[0],
                self.food.position[1],
                Config.BLOCK_SIZE,
                Config.BLOCK_SIZE
            )
        )
        
        self.show_score()
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_input()
            self.snake.update()

            # Check if snake ate food
            if (self.snake.position[0] == self.food.position[0] and 
                self.snake.position[1] == self.food.position[1]):
                self.score += 10
                self.snake.grow()
                self.food.spawn_new()
            else:
                self.snake.move()

            # Check collision
            if self.snake.check_collision():
                self.show_game_over()
                self.running = False
                break

            self.draw()
            self.clock.tick(Config.SNAKE_SPEED)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()