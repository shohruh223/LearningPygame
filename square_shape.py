import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((700, 800))

red = pygame.Color(255, 0, 0)
kvadrat_size = 50


def draw_shapes(x, y):
    shapes = [
        [[1, 1], [1, 1]],  # Kvadrat blok
    ]

    colors = [
        (0, 255, 0),  # Kvadrat blok
    ]

    for shape, color in zip(shapes, colors):
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j]:
                    rect = pygame.Rect(x + j * kvadrat_size, y + i * kvadrat_size, kvadrat_size, kvadrat_size)
                    pygame.draw.rect(screen, color, rect)
                    pygame.draw.rect(screen, (0, 0, 0), rect, 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    draw_shapes(100, 100)
    pygame.display.update()
