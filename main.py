import pygame
import random
import math
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Game Space")

# Background
# https://www.freepik.com/search?format=search&query=space%20background
background = pygame.image.load("image/background.jpg")

# Background Sound
mixer.music.load('music/background.wav')
mixer.music.play(-1)

#ushbu site dan space_with_pygame rasmni oldim
# https://www.flaticon.com/search?word=spaceship
icon = pygame.image.load("image/title.png")
pygame.display.set_icon(icon)


# Player raketa
# https://www.flaticon.com/search?word=arcade%20space  || raketani rasmi
playerImg = pygame.image.load("image/player.png")
playerX = 370 # o'yin boshlangan raketa o'rtada turishi. O'ng chap tomondan
playerY = 500  # o'yin boshlangan raketa o'rtada turishi. tepa past tomondan
playerX_change = 0  # o'yin boshlangan raketa o'rtada turishi, default holatda 0 bo'ladi

# enemy  sharpacha
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("image/enemy.png"))
    enemyX.append(random.randint(0, 735))  # o'yin boshlanganda sharpani qayerda turishi random qilindi, chap va o'ng
    enemyY.append(random.randint(50, 150))  # o'yin boshlanganda sharpani qayerda turishi random qilindi, tepa va past
    enemyX_change.append(4)  # o'yin boshlanganda sharpani ilk tezligi
    enemyY_change.append(40)   # sharpani pastga tushish o'lchami


# https://www.flaticon.com/search?word=bullet
# bullet
# Ready - You can't see the bullet on the scren
# Fire - The bullet is currently moving
bulletImg = pygame.image.load("image/bullet.png")  # bullet yani o'q rasmi
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5 # o'qni tezligi, pastdan tepaga
bullet_state = "ready"

# Font
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 255, 0))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):  # raketani harakatlanish funksiyasi
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):  # sharpani harakatlanish funksiyasi
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):  # o'qni harakatlanish funksiyasi
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):  # o'q tekkannini anglatuvchi funksiya
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#
# Game loop
flag = True
while flag:
    #ushbu site orqali rang xilma xilligini tanlang
    # https://www.rapidtables.com/convert/color/
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))
    # backgound image
    screen.blit(background, (0, 0))

    # playerX += 0.4 # o'nga
    # playerX -= 0.4 # chapga
    # playerY += 0.4 # pastga
    # playerY -= 0.4 # tepaga

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # x tugmasini bosganda dastur tugaydi
            flag = False

        # button right and left
        if event.type == pygame.KEYDOWN:  # chapga yurish tugmasi
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:  # o'nga yurish tugmasi
                playerX_change = 4
            if event.key == pygame.K_SPACE:   # otish tugmasi, space_with_pygame tugmasi bosiladi
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('music/laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change  # raketani o'nga chapga chegaralash
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]   # sharpani o'nga chapga chegaralash va uning keyingi tezligi
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1.2
            enemyY[i] += enemyY_change[i]

        # Collision  o'q tekkanini bildirib turish
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('music/explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 735)  # o'q tekkanda orqaga qaytish
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet
    if bulletY <= 0: # o'qni davomiyligini ta'minlash
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":  # o'q otish
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
