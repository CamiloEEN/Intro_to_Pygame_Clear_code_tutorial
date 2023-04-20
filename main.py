import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Rsc\Font\Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Rsc\Figs\Sky.png').convert()
ground_surface = pygame.image.load('Rsc\Figs\ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64) ).convert()
score_rect = score_surf.get_rect(center =(400,50))

snail_surface = pygame.image.load('Rsc\Figs\snail\snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))


player_surface = pygame.image.load('Rsc\Figs\Player\player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    # pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100) )
    screen.blit(score_surf,score_rect)
    
    snail_rect.right -=4
    if (snail_rect.right <= -50): snail_rect.right =800

    screen.blit(snail_surface,snail_rect)
    player_rect.left += 1
    screen.blit(player_surface,player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    #if player_rect.colliderect(snail_rect):
    #    print('Collision hapenned')

    # mouse_pos = pygame.mouse.get_pos()
    # if event.type == pygame.MOUSEBUTTONDOWN and player_rect.collidepoint(mouse_pos):
    #     print('you are clicking on the player')

    pygame.display.update()
    clock.tick(60)