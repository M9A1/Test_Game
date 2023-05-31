import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.group = game.all_sprites
        self.group.add(self)
        self.image = pg.transform.scale(pg.image.load("../data/characters/cat.png").convert_alpha(), (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.flipped = False
        
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y += -PLAYER_MOVE
        if keys[pg.K_a] and self.rect.x > 0:
            self.rect.x += -PLAYER_MOVE
        if keys[pg.K_s] and self.rect.y < SCREEN_HEIGHT - PLAYER_HEIGHT:
            self.rect.y += PLAYER_MOVE
        if keys[pg.K_d] and self.rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x += PLAYER_MOVE
        

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        