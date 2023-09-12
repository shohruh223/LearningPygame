import pygame


pygame.init()

# windows
oyna = pygame.display.set_mode((600, 600))

# Title
pygame.display.set_caption("Pygame shox")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # O'yin logikasi va qaydlarini shu yerdan davom ettirishingiz mumkin

    # Ekran rasmini yangilash
    pygame.display.update()

# O'yin tugadi
pygame.quit()
