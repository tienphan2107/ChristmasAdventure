import pygame


class Gift(pygame.sprite.Sprite):  # Sprite là lớp giúp chúng ta kiểm soát, điều chỉnh các đối tượng
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.surface.Surface((size, size))
        self.image = pygame.image.load('graphics/gift/gift.png')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, scroll_speed):
        self.rect.x += scroll_speed