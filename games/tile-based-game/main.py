import pygame
from pygame.locals import *

pygame.init()

screen_width = 1024
screen_height = 900

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#load images
sun_img = pygame.image.load('img/sun.jpg')
bg_img = pygame.image.load('img/sky.jpg')

tile_size = 200

def draw_grid():
    for line in range(0,0):
        pygame.draw.line(screen, (255,255,255), (0, line*tile_size), (screen_width, line*tile_size))
        pygame.draw.line(screen, (255,255,255), (line* tile_size, 0), (line*tile_size, screen_height))

run = True
while run:

    screen.blit(sun_img, (100,100))
    screen.blit(bg_img,(10,10))

    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()