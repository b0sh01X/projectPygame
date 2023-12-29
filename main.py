import os
import sys

import pygame
import random


pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Охота на роботов")


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Oxotnik(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.init()
    
    def init(self):
        sp = ['oxot-1.png', 'oxot-2.png', 'oxot-3.png']
        self.photo = random.choice(sp)
        self.image = pygame.transform.scale(load_image(self.photo), (150, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 0
    
    def strel(self):
        pulya = Pulya(pulya_gr)
        if self.photo == 'oxot-1.png':
            coord = (self.rect.x, self.rect.y + 28)
            pulya.strel(coord)


class Fon(pygame.sprite.Sprite):
    def __init__(self, group, fon):
        super().__init__(group)
        self.fon(fon)

    def fon(self, nomer):
        sp = ['fon.png', 'zastavka.png']
        self.image = pygame.transform.scale(load_image(sp[nomer - 1]), (1000, 600))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class Knopka(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image('knopka.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 450


class Pulya(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.image = pygame.transform.scale(load_image('pulya.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def strel(self, coord):
        self.rect.x = coord[0]
        self.rect.y = coord[1]
        while self.rect.x > 0:
            fon.draw(screen)
            self.rect.x -= 10
            pulya_gr.draw(screen)
            pygame.display.flip()
            pygame.time.Clock().tick(50)
        self.rect.x = -100


running = True
group = pygame.sprite.Group()
fon = pygame.sprite.Group()
zastav = pygame.sprite.Group()
pulya_gr = pygame.sprite.Group()
in_game = False

fon_game = Fon(fon, 1)
zastavka = Fon(zastav, 2)
kn = Knopka(zastav)

oxot = Oxotnik(group)
zerk1 = False
zastav.draw(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if in_game:
                if event.key == pygame.K_UP:
                    oxot.rect.y -= 10
                if event.key == pygame.K_DOWN:
                    oxot.rect.y += 10
                if event.key == pygame.K_SPACE:
                    oxot.strel()

        if event.type == pygame.MOUSEBUTTONDOWN and kn.rect.collidepoint(event.pos):
            in_game = True
            screen.fill((0, 0, 0))
    if in_game:
        fon.draw(screen)
        group.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(50)
pygame.quit()