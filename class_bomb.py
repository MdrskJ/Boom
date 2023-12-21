import pygame
import pygame.sprite
from random import randint
from consts import W, H, NORM_B_IMAGE, BOOM_B_IMAGE


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = NORM_B_IMAGE
        self.image_boom = BOOM_B_IMAGE
        self.rect = self.image.get_rect()
        self.w = self.rect.width
        self.h = self.rect.height
        self.rect.x = randint(0, W - self.w)
        self.rect.y = randint(0, H - self.h)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            w_boom = self.image_boom.get_rect().width
            h_boom = self.image_boom.get_rect().height
            self.rect.x -= abs((w_boom - self.w) // 2)
            self.rect.y -= abs((h_boom - self.h) // 2)
            self.image = self.image_boom
