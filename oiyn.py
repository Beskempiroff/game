import pygame, random

pygame.init()

# variables and constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
HEADER_HEIGHT = 80

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)

BUFFER_DISTANCE = 100
PLAYER_STARTING_SCORE = 0
PLAYER_STARTING_LIVE = 5
GHOSTPCK_STARTING_VELOCITY = 5

YELLOWGHOSTCUT_STARTING_VELOCITY = 9

player_score = PLAYER_STARTING_SCORE
player_live = PLAYER_STARTING_LIVE
cut_velocity = 5
ghostpck_velocity = GHOSTPCK_STARTING_VELOCITY

yellowghostcut_velocity = YELLOWGHOSTCUT_STARTING_VELOCITY
acceleration = 0.5

# main surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CuT")

# images
background = pygame.image.load('fon.jpeg')



score_backround = pygame.image.load('score_background.png').convert_alpha()
score_background_rect = score_backround.get_rect()
score_background_rect.topleft = (10,10)

live_background = pygame.image.load('score_background.png').convert_alpha()
live_background_rect = live_background.get_rect()
live_background_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width+10), 10)

cut_image = pygame.image.load('glv.PNG').convert_alpha()
cut_image = pygame.transform.scale(cut_image, (50, 80))  
cut_rect = cut_image.get_rect()
cut_rect.center = (80, WINDOW_HEIGHT//2)

ghostpck_image = pygame.image.load('dop.PNG').convert_alpha()
ghostpck_image = pygame.transform.scale(ghostpck_image, (40, 60)) 
ghostpck_image_rect = ghostpck_image.get_rect()
ghostpck_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))




yellowghostcut_image = pygame.image.load('bbom.png').convert_alpha()
yellowghostcut_image = pygame.transform.scale(yellowghostcut_image, (40, 60)) 
yellowghostcut_image_rect = yellowghostcut_image.get_rect()
yellowghostcut_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))



# fonts and texts
main_font = pygame.font.Font('AttackGraffiti.ttf', 32)

score_text = main_font.render("BALL: " + str(player_score), True, RED)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (20, 20)

game_name = main_font.render("CuT", True, RED, WHITE)
game_name_rect = game_name.get_rect()
game_name_rect.center = (WINDOW_WIDTH//2, HEADER_HEIGHT//2)

live_text = main_font.render("OIRI: " + str(player_live), True, RED)
live_text_rect = live_text.get_rect()
live_text_rect.topleft = (WINDOW_WIDTH-(live_background_rect.width), 20)

game_over_text = main_font.render("OIYN AYAQTALDY", True, GREEN, DARKGREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

game_continue_text = main_font.render("QAITADAN", True, GREEN)
game_continue_rect = game_continue_text.get_rect()
game_continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2+100)

 # sounds and musics
pygame.mixer.music.load('music.wav')
sound1 = pygame.mixer.Sound('sound_1.wav')
sound2 = pygame.mixer.Sound('sound_2.wav')
sound2.set_volume(0.1)

FPS = 60
clock = pygame.time.Clock()

pygame.mixer.music.play(-1, 0.0)
# main loop
fl_pause = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and cut_rect.top > HEADER_HEIGHT:
        cut_rect.y -= ghostpck_velocity
    elif keys[pygame.K_DOWN] and cut_rect.bottom < WINDOW_HEIGHT:
        cut_rect.y += ghostpck_velocity

    ghostpck_image_rect.centerx -= ghostpck_velocity
    yellowghostcut_image_rect.centerx -= yellowghostcut_velocity


    if ghostpck_image_rect.centerx < 0:
        ghostpck_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        player_live -= 1
        sound2.play()

    if yellowghostcut_image_rect.centerx < 0:
        yellowghostcut_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        player_live -= 0
        sound2.play()




    if cut_rect.colliderect(ghostpck_image_rect):
        player_score += 1
        sound1.play()
        ghostpck_image_rect.center = ((WINDOW_WIDTH+BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        ghostpck_velocity += acceleration

    
    if cut_rect.colliderect(yellowghostcut_image_rect):
        player_score -= 2
        player_live -= 5
        sound1.play()
        yellowghostcut_image_rect.center = ((WINDOW_WIDTH-BUFFER_DISTANCE), random.randint(HEADER_HEIGHT+25, WINDOW_HEIGHT-25))
        yellowghostcut_velocity += acceleration

        
    if player_live == 0 or player_score >15:
        fl_pause = True
        pygame.mixer.music.stop()
        live_text = main_font.render("ZHANY: " + str(player_live), True, RED)
        display_surface.blit(live_text, live_text_rect)
        pygame.display.update()
        while fl_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fl_pause = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    player_score = PLAYER_STARTING_SCORE
                    player_live = PLAYER_STARTING_LIVE
                    ghostpck_velocity = GHOSTPCK_STARTING_VELOCITY
                    yellowghostcut_velocity = GHOSTPCK_STARTING_VELOCITY
                    pygame.mixer.music.play(-1, 0.0) 
                    fl_pause = False

            display_surface.blit(game_over_text, game_over_rect)
            display_surface.blit(game_continue_text, game_continue_rect)
            pygame.display.update()


    display_surface.blit(background, (0,0))
    display_surface.blit(score_backround, score_background_rect)
    display_surface.blit(live_background, live_background_rect)
    pygame.draw.line(display_surface, WHITE, (0, HEADER_HEIGHT), (WINDOW_WIDTH, HEADER_HEIGHT), 5)
    display_surface.blit(cut_image, cut_rect)
    display_surface.blit(ghostpck_image, ghostpck_image_rect)
    display_surface.blit(yellowghostcut_image, yellowghostcut_image_rect)
    
    score_text = main_font.render("OCHKO: " + str(player_score), True, RED)
    live_text = main_font.render("ZHANY: " + str(player_live), True, RED)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(game_name, game_name_rect)
    display_surface.blit(live_text, live_text_rect)
    


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()