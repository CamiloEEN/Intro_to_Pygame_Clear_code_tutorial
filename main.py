import pygame
from sys import exit

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surf = test_font.render(str(current_time), False, (64,64,64) )
    score_rect = score_surf.get_rect(center =(400,50))
    screen.blit(score_surf,score_rect)
    

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Rsc\Font\Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('Rsc\Figs\Sky.png').convert()
ground_surface = pygame.image.load('Rsc\Figs\ground.png').convert()
ground_level=300

# score_surf = test_font.render('My game', False, (64,64,64) ).convert()
# score_rect = score_surf.get_rect(center =(400,50))

snail_surface = pygame.image.load('Rsc\Figs\snail\snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,ground_level))


player_surface = pygame.image.load('Rsc\Figs\Player\player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,ground_level))
player_fall_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not (game_active):
            if event.type == pygame.KEYDOWN:
                game_active = True
                snail_rect.right =800
                player_rect.left=0
                start_time = pygame.time.get_ticks()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(pygame.mouse.get_pos()) and player_rect.bottom == ground_level:
                    player_fall_speed=-20
                    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == ground_level:
                    player_fall_speed=-20

            if event.type == pygame.KEYUP:
                print('key up')
        
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,ground_level))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # screen.blit(score_surf,score_rect)
        display_score()
        
        # Snail
        snail_rect.right -=4
        if (snail_rect.right <= -50): snail_rect.right =800
        screen.blit(snail_surface,snail_rect)

        # Player
        player_rect.left += 1
        if player_rect.left >=800: player_rect.left=0
        # due to y axis increasing downwards player_rect.bottom < ground_level is well written
        if player_rect.bottom < ground_level:
            player_fall_speed += 1
        elif player_rect.bottom > ground_level:
            player_rect.bottom = ground_level
            player_fall_speed = 0

        player_rect.y += int(player_fall_speed)
        screen.blit(player_surface,player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            print('Game over')
            game_active = False

    else:
        screen.fill("Yellow")
    pygame.display.update()
    clock.tick(60)