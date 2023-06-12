import pygame
from setting import *


class Decorate(pygame.sprite.Sprite):
    def __init__(self, pos,size,  index):
        super().__init__()
        self.image = pygame.surface.Surface((size,size))
        self.image = pygame.image.load(tile_directory[index])
        # self.image.fill('green')
        self.rect = self.image.get_rect(topleft=pos)  # chuyển image của 1 block thành dạng hcn có tọa độ

    def update(self, scroll_speed):  # cái này di màn hình khi đi gần hết map
        self.rect.x += scroll_speed
