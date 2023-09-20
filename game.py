import pygame
import random

# Pygame'ni boshlang'ichini o'rnatish
pygame.init()
# O'yin oynasini yaratish va o'lchamini aniqlash
screen = pygame.display.set_mode((400, 400))

# Balon ranglarini aniqlash (qizil, yashil, ko'k)
balloon_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # red, green, blue
# Balonning eni va balandligini aniqlash
balloon_width = 20
balloon_height = 30
# Balonlar sonini aniqlash
num_balloons = 10

# Balonlar haqida ma'lumotlarni saqlash uchun ro'yxat yaratish
balloons = []

# Balonlarni chizish
for i in range(num_balloons):
    x = random.randint(0, screen.get_width() - balloon_width)
    y = random.randint(screen.get_height() // 2, screen.get_height() - balloon_height)
    color = random.choice(balloon_colors)
    balloon_rect = pygame.draw.ellipse(screen, color, (x, y, balloon_width, balloon_height))

    # Dum qismini chizish
    tail_start_x = x + balloon_width // 2
    tail_start_y = y + balloon_height
    tail_end_x = tail_start_x
    tail_end_y = tail_start_y + random.randint(10, +20)
    pygame.draw.line(screen, color, (tail_start_x, tail_start_y), (tail_end_x, tail_end_y))

    balloons.append((balloon_rect, color))

# Hisoblagichni boshlash
counter = 0

# Matn ko'rsatish uchun font obyektini yaratish
font = pygame.font.Font(None, 36)

# Ekran yangilanishini o'zgartirish
pygame.display.flip()

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Tugma bosilganda
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i in range(len(balloons)):
                balloon_rect, color = balloons[i]
                if balloon_rect.collidepoint(mouse_pos):
                    # Balonni ro'yxatdan olib tashlash
                    balloons.pop(i)

                    # Hisoblagichni oshirish
                    counter += 1

                    break

    # Balonlarni yuqoriga ko'tarish
    for i in range(len(balloons)):
        balloon_rect, color = balloons[i]
        balloon_rect.move_ip(0, -5)
        if balloon_rect.bottom < 0:
            # Balonni ekranning pastki qismiga ko'chirish
            balloon_rect.bottom = screen.get_height()

    # Ekran bilan tozalash
    screen.fill((255, 255, 255))

    # Balonlarni va ularning orqa chiziqlarini qayta chizish
    for i in range(len(balloons)):
        balloon_rect, color = balloons[i]

        pygame.draw.ellipse(screen, color, balloon_rect)

        # Balon kvadratining orqa chiziqqa bog'langan qismi
        tail_start_x = balloon_rect.x + balloon_width // 2
        tail_start_y = balloon_rect.y + balloon_height
        tail_end_x = tail_start_x
        tail_end_y = tail_start_y + random.randint(10, +20)
        pygame.draw.line(screen, color, (tail_start_x, tail_start_y), (tail_end_x, tail_end_y))

    # Hisobni ekran ostida ko'rsatish
    score_text = font.render("Score: " + str(counter), True, (0, 0, 0))
    screen.blit(score_text, (5, 5))

    # update the display
    pygame.display.flip()

    # wait for a while
    pygame.time.wait(100)