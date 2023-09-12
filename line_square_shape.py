import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen size and create a screen object
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the block size and color
block_size = 50
block_color = (0, 255, 255)  # Cyan


# Draw a Tetris rectangle on the screen
def draw_rectangle(x, y):
    for i in range(4):
        rect = pygame.Rect(x + i * block_size, y, block_size, block_size)
        pygame.draw.rect(screen, block_color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 1)


# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a Tetris rectangle on the screen
    draw_rectangle(100, 100)

    # Update the screen
    pygame.display.update()