import pygame
from pygame import Color, sprite

from class_bomb import Bomb
from consts import SIZE


def main():
    pygame.init()
    sc = pygame.display.set_mode(SIZE)

    all_sprites = sprite.Group()
    for _ in range(20):
        Bomb(all_sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in all_sprites:
                    bomb.update(event)

        sc.fill(Color('black'))
        all_sprites.draw(sc)
        all_sprites.update()
        pygame.display.flip()


if __name__ == '__main__':
    main()
