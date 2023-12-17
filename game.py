import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Variabel konstanta
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_SIZE = 20
FPS = 10

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inisialisasi layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Inisialisasi snake
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (GRID_SIZE, 0)

# Inisialisasi makanan
food = (random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
        random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE)

# Fungsi untuk menggambar snake dan makanan
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

# Fungsi utama game
def game_loop():
    global snake
    global snake_direction
    global food

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, GRID_SIZE):
                    snake_direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -GRID_SIZE):
                    snake_direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT and snake_direction != (GRID_SIZE, 0):
                    snake_direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-GRID_SIZE, 0):
                    snake_direction = (GRID_SIZE, 0)

        # Update snake position
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)

        # Check collision with food
        if snake[0] == food:
            food = (random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
                    random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE)
        else:
            snake.pop()

        # Check collision with walls or itself
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]):
            pygame.quit()
            sys.exit()

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw snake and food
        draw_snake(snake)
        draw_food(food)

        # Update display
        pygame.display.flip()

        # Set FPS
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
