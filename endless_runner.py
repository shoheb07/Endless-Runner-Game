import pygame
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player
player = pygame.Rect(100, 300, 50, 50)

jump = False
jump_count = 10

# Obstacles
obstacles = []

clock = pygame.time.Clock()

score = 0

font = pygame.font.SysFont(None, 40)

running = True

while running:

    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                jump = True

    # Jump Logic
    if jump:

        player.y -= jump_count * 2

        jump_count -= 1

        if jump_count < -10:

            jump = False

            jump_count = 10

    # Generate Obstacles
    if random.randint(1, 60) == 1:

        obstacle = pygame.Rect(
            WIDTH,
            310,
            30,
            40
        )

        obstacles.append(obstacle)

    # Move Obstacles
    for obstacle in obstacles:

        obstacle.x -= 6

        pygame.draw.rect(
            screen,
            BLACK,
            obstacle
        )

        if obstacle.colliderect(player):

            running = False

    # Draw Player
    pygame.draw.rect(
        screen,
        (0, 150, 255),
        player
    )

    # Increase Score
    score += 1

    score_text = font.render(
        f"Score: {score}",
        True,
        BLACK
    )

    screen.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
