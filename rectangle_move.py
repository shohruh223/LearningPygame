import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

# Define the player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(200, 150, 30, 30)
        self.color = (0, 255, 0)

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 3
        if key[pygame.K_RIGHT]:
            self.rect.x += 3
        if key[pygame.K_UP]:
            self.rect.y -= 3
        if key[pygame.K_DOWN]:
            self.rect.y += 3

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

# Define the enemy class
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, 370), random.randint(0, 270), 30, 30)
        self.color = (255, 0, 0)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

player = Player()
enemies = [Enemy() for _ in range(10)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_keys()

    screen.fill((0, 0, 0))
    player.draw()
    for enemy in enemies:
        enemy.draw()
        if player.rect.colliderect(enemy.rect):
            print("Collision detected!")
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()