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


def load_robot():
    sp = [False, True]
    r = random.choice(sp)
    if r:
        Robot()


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
        if self.photo == 'oxot-1.png':
            coord = (self.rect.x, self.rect.y + 75)
            Pulya(coord)
        if self.photo == 'oxot-2.png':
            coord = (self.rect.x, self.rect.y + 75)
            Pulya(coord)
        if self.photo == 'oxot-3.png':
            coord = (self.rect.x, self.rect.y + 65)
            Pulya(coord)


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
    def __init__(self, coord):
        super().__init__(pulya_gr)
        self.image = pygame.transform.scale(load_image('pulya.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]
    
    def update(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.kill()


class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(rabot)
        self.image = pygame.transform.scale(load_image('robot.png'), (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = -70
        self.rect.y = random.randrange(-60, 600)
    
    def update(self, killall=False):
        global in_game
        global verx
        global vniz
        self.rect.x += 3
        if killall:
            self.kill
        if self.rect.x > 900:
            in_game = False
            group.update(True)
            self.kill()
            vniz = False
            verx = False


running = True
count = 0
group = pygame.sprite.Group()
fon = pygame.sprite.Group()
zastav = pygame.sprite.Group()
pulya_gr = pygame.sprite.Group()
rabot = pygame.sprite.Group()
in_game = False
verx = False
vniz = False

fon_game = Fon(fon, 1)
zastavka = Fon(zastav, 2)
kn = Knopka(zastav)

oxot = Oxotnik(group)
zerk1 = False
while running:
    zastav.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if in_game:
                if event.key == pygame.K_UP:
                    verx = True
                if event.key == pygame.K_DOWN:
                    vniz = True
                if event.key == pygame.K_SPACE:
                    oxot.strel()
        if event.type == pygame.KEYUP:
            if in_game:
                if event.key == pygame.K_UP:
                    verx = False
                if event.key == pygame.K_DOWN:
                    vniz = False
        if event.type == pygame.MOUSEBUTTONDOWN and kn.rect.collidepoint(event.pos):
            in_game = True
            screen.fill((0, 0, 0))
    if in_game:
        fon.draw(screen)
        group.draw(screen)
        pulya_gr.draw(screen)
        pulya_gr.update()
        rabot.update()
        rabot.draw(screen)
        if count == 100:
            load_robot()
            count = 0
        else:
            count += 1
        if verx:
            oxot.rect.y -= 5
        if vniz:
            oxot.rect.y += 5
    pygame.display.flip()
    pygame.time.Clock().tick(50)
pygame.quit()