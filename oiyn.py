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


player_score = PLAYER_STARTING_SCORE
player_live = PLAYER_STARTING_LIVE
cut_velocity = 5

# main surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CuT")

# images
background = pygame.image.load('fon.jpeg')



cut_image = pygame.image.load('glv.PNG').convert_alpha()
cut_image = pygame.transform.scale(cut_image, (50, 80))  
cut_rect = cut_image.get_rect()
cut_rect.center = (80, WINDOW_HEIGHT//2)







# fonts and texts
main_font = pygame.font.Font('AttackGraffiti.ttf', 32)





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


        
    if player_live == 0 or player_score >15:
        fl_pause = True
        pygame.mixer.music.stop()
        live_text = main_font.render("ZHANY: " + str(player_live), True, RED)
        pygame.display.update()
        while fl_pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fl_pause = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    player_score = PLAYER_STARTING_SCORE
                    player_live = PLAYER_STARTING_LIVE
                    pygame.mixer.music.play(-1, 0.0) 
                    fl_pause = False

      
     
            pygame.display.update()


    display_surface.blit(background, (0,0))
    pygame.draw.line(display_surface, WHITE, (0, HEADER_HEIGHT), (WINDOW_WIDTH, HEADER_HEIGHT), 5)
    display_surface.blit(cut_image, cut_rect)

    



    


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()