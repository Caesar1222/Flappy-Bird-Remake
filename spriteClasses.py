### Sprite classes for Game ###
import pygame

class Pipe(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y, rotation):
        super().__init__()
        ### Pipe Sprite ###
        if rotation == 0:
            self.image = pygame.image.load('Flappy bird/Images/Mpip.png')
        else:
            self.image = pygame.image.load('Flappy bird/Images/MLpip.png')
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def update(self):
        self.rect.x -= 10

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        ### Player Sprites ###
        self.sprites = [pygame.image.load("Flappy bird/Images/qrame-2.png"), pygame.image.load("Flappy bird/Images/qrame-3.png"), pygame.image.load("Flappy bird/Images/qrame-4.png")]
        self.is_animating = False

        ### Player Sprite Setup ###
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        ### Initial player physics ###
        self.velocity = 0
        self.gravity = 0.25

    def update_position(self): 
        ### Player Physics over time ###
        self.velocity += self.gravity
        self.rect.y += self.velocity

    ### Animation trigger###
    def animate(self):
        self.is_animating = True

    def update(self):
        ### Animation ###
        if self.is_animating == True:
            self.current_sprite += 0.2
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0 
                self.is_animating = False
            ### Changing sprite image to create animation ###
            self.image = self.sprites[int(self.current_sprite)]
