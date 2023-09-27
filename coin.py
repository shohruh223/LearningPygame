import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((600, 600))

# Set title
pygame.display.set_caption("Coin Collector")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set font
font = pygame.font.Font(None, 36)

# Load player and coin images
player_image = pygame.image.load("basket.jpeg")
coin_image = pygame.image.load("coin.png")

# Create player sprite
player = pygame.sprite.Sprite()
player.image = player_image
player.rect = player.image.get_rect()
player.rect.centerx = 300
player.rect.bottom = 550

# Create coin sprite group
coins = pygame.sprite.Group()


# Create coin sprite
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 575)
        self.rect.y = -25

    def update(self):
        self.rect.y += 3
        if self.rect.top > 600:
            self.kill()


# Set score and time
score = 0
time_left = 30

# Set game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5

    # Keep player on screen
    if player.rect.left < 0:
        player.rect.left = 0
    if player.rect.right > 600:
        player.rect.right = 600

    # Add new coin
    if random.randint(1, 30) == 1:
        coins.add(Coin())

    # Update coins
    coins.update()

    # Check for collision with coins
    hit_list = pygame.sprite.spritecollide(player, coins, True)
    for coin in hit_list:
        score += 1

    # Update time left
    time_left -= 1 / 60

    # Draw screen
    screen.fill(WHITE)

    # Draw player and coins
    screen.blit(player.image, player.rect)
    coins.draw(screen)

    # Draw score and time left
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (450, 10))
    text = font.render("Time left: " + str(int(time_left)), True, BLACK)
    screen.blit(text, (450, 40))
    # Check for game over
    if time_left <= 0:
        done = True

    # Update screen
    pygame.display.flip()
    print('Your score ' + str(score))

# Quit Pygame
pygame.quit()
