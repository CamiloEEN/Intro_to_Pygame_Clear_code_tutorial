import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Rsc\Font\Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Rsc\Figs\Sky.png').convert()
ground_surface = pygame.image.load('Rsc\Figs\ground.png').convert()
test_surface = test_font.render('My game', False, 'Black' ).convert()

snail_surface = pygame.image.load('Rsc\Figs\snail\snail1.png').convert_alpha()
snail_x_pos = 600

player_surface = pygame.image.load('Rsc\Figs\Player\player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(test_surface,(300,50))
    snail_x_pos -=4
    if (snail_x_pos <= -50): snail_x_pos =800

    screen.blit(snail_surface,(snail_x_pos,250))
    player_rect.left += 1
    screen.blit(player_surface,player_rect)

    pygame.display.update()
    clock.tick(60)