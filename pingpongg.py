import pygame
import sys
import random

# Ініціалізація Pygame
pygame.init()

# Константи
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
FPS = 60
WHITE = (255, 255, 255)

# Створення вікна гри
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пінг-Понг")

# Створення ракеток та м'яча
player1_rect = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_rect = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball_rect = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

# Початкові швидкості м'яча
ball_speed_x = random.choice([1, -1]) * 5
ball_speed_y = random.choice([1, -1]) * 5

# Задержка перед грою
pygame.time.delay(1000)

# Функція оновлення гри
def update():
    global ball_speed_x, ball_speed_y

    # Рух м'яча
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Відбиття м'яча від верхньої та нижньої межі екрану
    if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Відбиття м'яча від ракеток
    if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
        ball_speed_x = -ball_speed_x

    # Перевірка програшу
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        pygame.quit()
        sys.exit()

# Головний цикл гри
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Оновлення гри
    update()

    # Обрисовка екрану
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player1_rect)
    pygame.draw.rect(screen, WHITE, player2_rect)
    pygame.draw.ellipse(screen, WHITE, ball_rect)

    # Управління ракетками гравців
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_rect.top > 0:
        player1_rect.y -= 5
    if keys[pygame.K_s] and player1_rect.bottom < HEIGHT:
        player1_rect.y += 5
    if keys[pygame.K_UP] and player2_rect.top > 0:
        player2_rect.y -= 5
    if keys[pygame.K_DOWN] and player2_rect.bottom < HEIGHT:
        player2_rect.y += 5

    # Оновлення екрану
    pygame.display.flip()

    # Задержка для досягнення необхідного FPS
    clock.tick(FPS)
