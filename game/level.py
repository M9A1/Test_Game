import pygame as pg
from settings import *


class Level:
    def __init__(self, background: str):
        self.image = pg.transform.scale(pg.image.load(f"../data/tiles/{background}.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        
    def draw(self, screen: pg.Surface):
        screen.blit(self.image, (0, 0))
        