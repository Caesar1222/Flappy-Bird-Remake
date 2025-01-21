from spriteClasses import Pipe, Player
import pygame
import random
import sys
import math

### Initial Variables ###
pygame.init()
run = True
update_position = False
score = 0 
x = 0

### General Setup ###
pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 457
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("Flappy bird/Images/BG.png")
scroll = 0
tiles = math.ceil(screen_width / background.get_width()) + 1

### Player sprite ###
player_group = pygame.sprite.Group()
player = Player((screen_width / 8), (screen_height / 2))
player_group.add(player) 

### Pipe sprites ###
pipeupper_pos = random.randint(0,140)
pipeupper = Pipe((screen_width), (pipeupper_pos), 0)
pipelower = Pipe((screen_width), (pipeupper_pos + 450), 1)
pipe_group = pygame.sprite.Group()
pipe_group.add(pipelower)
pipe_group.add(pipeupper)

### Game loop ###
while run: 
    player.update()
    keys = pygame.key.get_pressed()  # Check for key presses inside the loop

    ### check if player hits top of screen or bottom of screen ###
    if player.rect.y <= 10 or player.rect.y >= 390:
        sys.exit()

    if pipeupper.rect.x == 10:
        score + 1
        pipe_group.empty()

        if str(pipe_group) == "<Group(0 sprites)>":
            pipeupper_pos = random.randint(-90,140)
            pipeupper = Pipe((screen_width + 10), (pipeupper_pos), 0)
            pipelower = Pipe((screen_width + 10), (pipeupper_pos + 470), 1)
            pipe_group.add(pipelower)
            pipe_group.add(pipeupper)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            update_position = True
            player.animate()
            player.velocity = 0
            player.velocity -= 8

    ### Collision Detection ###
    for pipes in pipe_group:
        if pygame.sprite.collide_rect_ratio(0.9)(player, pipes):
            update_position = False
            scroll = False
            pygame.quit()
            
    ### Scrolling Background ###
    scroll -= 6
    screen.blit(background, (0, 0))  
    if abs(scroll) > background.get_width():
        scroll = 0
        score += 1 
        print(score) 
    
    ### Shifting background across screen (Right to Left) ###
    for i in range(0, tiles):
        screen.blit(background, (i * background.get_width() + scroll, 0))

    ### Updating Sprites ###
    if update_position:
        player.update_position()
        pipe_group.update()
    player_group.draw(screen)
    pipe_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)
