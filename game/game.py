"""
This program demonstrates blitting.
"""

import pygame as pg
import random

from sprites import *
from level import *
from settings import *

# while len(enemy_list) < MAX_ENEMIES:
#     enemy_rect = enemy_surface.get_rect()
#     enemy_rect.x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
#     enemy_rect.y = random.randint(0, SCREEN_HEIGHT - ENEMY_HEIGHT)
#     enemy_list.append(enemy_rect)

# for enemy in enemy_list:
#     pg.draw.rect(SCREEN, ENEMY_COLOR, enemy)

#     if player_rect.colliderect(enemy):
#         enemy_list.remove(enemy)
#         score += 1


class Game:
    def __init__(self):
        # Initialize Pygame and create window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.show_start_screen()
        self.all_sprites = pg.sprite.Group()
        self.level = Level("Grass_01")
        self.player = Player(self)
        self.run()
        self.show_game_over_screen()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.level.draw(self.screen)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_game_over_screen(self):
        pass


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.new()
        g.show_game_over_screen()

    pg.quit()
