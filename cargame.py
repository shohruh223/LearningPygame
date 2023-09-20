#tutorial: https://www.youtube.com/watch?v=W-QOtdD3qx4

# Pygame va boshqa zarur kutubxonalarni import qilamiz
import pygame
from pygame.locals import *
import random

# shaklning parametrlari
size = width, height = (800, 800)  # o'yin oynasining o'lchami
road_w = int(width/1.6)  # yo'lovning eni
roadmark_w = int(width/80)  # yo'l belgilari eni
# joylashish parametrlari
right_lane = width/2 + road_w/4  # o'ng yo'lni belgilash
left_lane = width/2 - road_w/4  # chap yo'lni belgilash
# animatsiya parametrlari
speed = 1  # harakat tezligi

# O'yinni boshlaymiz
pygame.init()
running = True

# O'yin oynasini o'lchamini sozlaymiz
screen = pygame.display.set_mode(size)
# O'yin oynasining sarlavhasini sozlaymiz
pygame.display.set_caption("Car game")
# Foni rangini sozlaymiz
screen.fill((60, 220, 0))
# O'zgarishlarni amalga oshiramiz
pygame.display.update()

# Foydalanuvchi transportini yuklaymiz
car = pygame.image.load("car.png")
# Tasvirni o'lchamini o'zgartiramiz
# car = pygame.transform.scale(car, (250, 250))
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8  # Transportni boshlang'ich joylashamiz

# Dushman transportini yuklaymiz
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2  # Dushman transportini boshlang'ich joylashamiz

counter = 0
# O'yin tsikli
while running:
    counter += 1

    # O'yin murakkabligini vaqti o'tganda oshiramiz
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("darajani oshirish", speed)

    # Dushman transportini animatsiyalash
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # Tasodifiy ravishda yo'l tanlaymiz
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # O'yin tugash shartlari
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("O'YIN TUGADI! SIZ YUTQAZDINGIZ!")
        break

    # Hodisalar tinglovchilari
    for event in pygame.event.get():
        if event.type == QUIT:
            # Dasturni yopamiz
            running = False
        if event.type == KEYDOWN:
            # Foydalanuvchi transportini chapga ko'chirish
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            # Foydalanuvchi transportini o'ngga ko'chirish
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])

    # Yo'lni chizamiz
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height))
    # Markaz chizmasini chizamiz
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height))
    # Chap yo'l belgilarini chizamiz
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # O'ng yo'l belgilarini chizamiz
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    # Transport tasvirlarini o'yin oynasiga joylashtiramiz
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # O'zgarishlarni amalga oshiramiz
    pygame.display.update()

# O'yin oynasini yopamiz
pygame.quit()
