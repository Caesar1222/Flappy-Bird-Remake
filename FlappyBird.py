from pygame import font
import pygame

import random
import time
import sys
import math
pygame.init()
x = 0
score = 0 

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, rotation):
        super().__init__()
        ### Pipe Sprite ###
        if rotation == 0:
            self.image = pygame.image.load('Flappy bird\Images\Mpip.png')
        else:
            self.image = pygame.image.load('Flappy bird\Images\MLpip.png')
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    ### Pipe physics
    def update(self):
        self.rect.x -= 10

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        super().__init__()
        ### Player Sprite ###
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("Flappy bird/Images/qrame-2.png"))
        self.sprites.append(pygame.image.load("Flappy bird/Images/qrame-3.png"))
        self.sprites.append(pygame.image.load("Flappy bird/Images/qrame-4.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.velocity = 0
        self.gravity = 0.25

    ### Player Physics ###
    def death(self):
        self.rect.y += self.gravity


    def update_position(self): 
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.velocity = 0

        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = abs(self.velocity*0.1 + 0.0000001)

    ### Animation ###
    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0 
                self.is_animating = False
            
            self.image = self.sprites[int(self.current_sprite)]

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1000
screen_height = 457
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("Flappy bird\Images\BG.png")

# Game variables
scroll = 0
tiles = math.ceil(screen_width / background.get_width()) + 1

# Player sprite 
player_group = pygame.sprite.Group()
player = Player((screen_width / 8), (screen_height / 2))
player_group.add(player) 

# Pipe sprite
pipeupper_pos = random.randint(0,140)
pipeupper = Pipe((screen_width), (pipeupper_pos), 0)
pipelower = Pipe((screen_width), (pipeupper_pos + 450), 1)

pipe_group = pygame.sprite.Group()
pipe_group.add(pipelower)
pipe_group.add(pipeupper)

# Game
run = True
update_position = False

while run: 
    player.update()
    keys = pygame.key.get_pressed()  # Check for key presses inside the loop

    if pipeupper.rect.x == 10:
        score + 1
        pipe_group.empty()

        if str(pipe_group) == "<Group(0 sprites)>":
            pipeupper_pos = random.randint(-90,140)
            pipeupper = Pipe((screen_width + 10), (pipeupper_pos), 0)
            pipelower = Pipe((screen_width + 10), (pipeupper_pos + 470), 1)
            pipe_group.add(pipelower)
            pipe_group.add(pipeupper)

    if player.rect.y <= 10:
        sys.exit()
    if player.rect.y >= 390:
        sys.exit()

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
    for each in pipe_group:
        if pygame.sprite.collide_rect_ratio(0.9)(player, each):
            update_position = False
            scroll = False
            pygame.quit()
            
    # Scroll background
    scroll -= 6
    # Reset Scroll
    if abs(scroll) > background.get_width():
        scroll = 0

    screen.blit(background, (0, 0))  # Draw the background first

    for i in range(0, tiles):
        screen.blit(background, (i * background.get_width() + scroll, 0))

    if update_position:
        player.update_position()
        pipe_group.update()

    player_group.draw(screen)  # Then draw the player sprite(s) on top of the background
    pipe_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)
