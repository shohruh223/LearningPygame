import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 600

# Set colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set player starting position
player_x = screen_width / 2
player_y = screen_height / 2

# Set player dimensions
player_width = 20
player_height = 20

# Set player speed
player_speed = 5

# Create list to store obstacles
obstacles = []

# Set obstacle dimensions
obstacle_width = 20
obstacle_height = 20

# Set obstacle speed
obstacle_speed = 3

# Set game over flag
game_over = False

# Set clock for frame rate
clock = pygame.time.Clock()

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move player based on pressed keys
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Check for collision with screen boundaries
    if player_x < 0:
        player_x = 0
    if player_x > screen_width - player_width:
        player_x = screen_width - player_width
    if player_y < 0:
        player_y = 0
    if player_y > screen_height - player_height:
        player_y = screen_height - player_height

    # Generate new obstacles at random intervals
    if random.randint(1, 50) == 1:
        # Set starting position for new obstacle
        obstacle_x = random.randint(0, screen_width - obstacle_width)
        obstacle_y = 0 - obstacle_height

        # Add new obstacle to list of obstacles
        obstacles.append([obstacle_x, obstacle_y])

    # Move obstacles down the screen and check for collision with player or bottom of screen
    for obstacle in obstacles:
        # Move obstacle down the screen
        obstacle[1] += obstacle_speed

        # Check for collision with bottom of screen
        if obstacle[1] > screen_height:
            obstacles.remove(obstacle)

        # Check for collision with player
        if (player_x < obstacle[0] + obstacle_width and
                player_x + player_width > obstacle[0] and
                player_y < obstacle[1] + obstacle_height and
                player_y + player_height > obstacle[1]):
            game_over = True

    # Fill screen with black color to erase previous frame
    screen.fill(black)

    # Draw obstacles on screen
    for obstacle in obstacles:
        pygame.draw.rect(screen, green, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))

    # Draw player on screen
    pygame.draw.rect(screen, red, (player_x, player_y, player_width, player_height))

    # Update display to show new frame
    pygame.display.update()

    # Control frame rate to limit speed of game loop
    clock.tick(60)

# Quit Pygame when game loop ends
pygame.quit()
