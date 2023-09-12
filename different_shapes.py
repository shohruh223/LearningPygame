import pygame
import random

# O'yinning o'lchamlari
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_SIZE = 25
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Ranglar
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tetromino shakllari
tetrominos = [
    [(1, 1, 1, 1)],            # I-shakli
    [(1, 1, 1, 0), (1,)],      # J-shakli
    [(1, 1, 1, 0), (0, 1)],    # L-shakli
    [(1, 1), (1, 1)],          # O-shakli
    [(1, 1, 1), (0, 1)],       # S-shakli
    [(1, 1, 1), (1, 0)],       # T-shakli
    [(1, 1, 1), (0, 0, 1)]     # Z-shakli
]

# Pygameni boshlash
pygame.init()

# O'yin oynasini yaratish
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Tetromino o'yin oynasi
def draw_tetromino(shape, x, y):
    for row, line in enumerate(shape):
        for col, cell in enumerate(line):
            if cell:
                pygame.draw.rect(
                    screen,
                    WHITE,
                    pygame.Rect((x + col) * GRID_SIZE, (y + row) * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                )

# O'yin boshlanish holati
def main():
    clock = pygame.time.Clock()
    current_tetromino = random.choice(tetrominos)
    x, y = GRID_WIDTH // 2 - 1, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 1
        if keys[pygame.K_RIGHT]:
            x += 1
        if keys[pygame.K_DOWN]:
            y += 1

        screen.fill(BLACK)
        draw_tetromino(current_tetromino, x, y)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
