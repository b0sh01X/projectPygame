import os
import sys

import pygame
import random


pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Охота на роботов")
r, g, b = 0, 0, 0
s_rgb = ['r', 'g', 'b']
pygame.mixer.music.load("data/music.mp3")
pygame.mixer.music.play(-1)


def countt():
    font = pygame.font.Font(None, 50)
    text = font.render(str(count_kill), True, (255, 255, 255))
    text_w = text.get_width()
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, text_w + 30, 50))
    screen.blit(text, (15, 10))


def zast(num=False):
    if num == False:
        font = pygame.font.Font(None, 100)
        text = font.render('Охота на роботов', True, (0, 255, 255))
        text_x = width // 2 - text.get_width() // 2
        text_y = (height // 2 - text.get_height() // 2) - 150
        screen.blit(text, (text_x, text_y))
    elif num == True:
        font = pygame.font.Font(None, 100)
        text = font.render('Игра окончена', True, (0, 255, 255))
        text_x = width // 2 - text.get_width() // 2
        text_y = (height // 2 - text.get_height() // 2) - 150

        font2 = pygame.font.Font(None, 50)
        text2 = font2.render(f'Со счётом {count_kill1}', True, (0, 255, 255))
        text2_x = (width // 2 - text.get_width() // 2) + 50
        text2_y = (height // 2 - text.get_height() // 2) - 50

        screen.blit(text, (text_x, text_y))
        screen.blit(text2, (text2_x, text2_y))


def restart():
    global kd_pulya
    global count
    global count_kill
    global rs
    global count_kill1
    count_kill1 = count_kill
    rs = True
    for i in all_sprites:
        i.kill()
    kn.restartt()
    kd_pulya = 25
    count_kill = 0
    count = 0
    pygame.mixer.music.stop()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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
        super().__init__(group, all_sprites)
        self.init()
        self.mask = pygame.mask.from_surface(self.image)
    
    def init(self):
        sp = ['oxot-1.png', 'oxot-2.png', 'oxot-3.png']
        self.photo = random.choice(sp)
        self.image = pygame.transform.scale(load_image(self.photo), (150, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 0
    
    def strel(self):
        global kd_pulya
        if kd_pulya > 25:
            kd_pulya = 0
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

    def restartt(self):
        self.image = pygame.transform.scale(load_image('restart.png'), (100, 100))


class Pulya(pygame.sprite.Sprite):
    def __init__(self, coord):
        super().__init__(pulya_gr, all_sprites)
        self.image = pygame.transform.scale(load_image('pulya.png'), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = coord[0]
        self.rect.y = coord[1]
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        global count_kill
        self.rect.x -= 20
        if self.rect.x < 0:
            self.kill()
        for r in rabot:
            if pygame.sprite.collide_mask(self, r):
                self.kill()
                r.kill()
                count_kill += 1


class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(rabot, all_sprites)
        self.image = pygame.transform.scale(load_image('robot.png'), (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = -70
        self.rect.y = random.randrange(0, 470)
        self.mask = pygame.mask.from_surface(self.image)
    
    def update(self):
        global in_game
        global verx
        global vniz
        global count_kill
        self.rect.x += 1 + count_kill
        if self.rect.x > 900 or pygame.sprite.collide_mask(self, oxot):
            in_game = False
            self.kill()
            vniz = False
            verx = False
            restart()


pygame.mixer.music.stop()
pygame.mixer.music.set_volume(100)
running = True
count = 0
kd_pulya = 25
count_kill = 0
count_kill1 = 0

icon = load_image('icon.png')
pygame.display.set_icon(icon)

group = pygame.sprite.Group()
fon = pygame.sprite.Group()
zastav = pygame.sprite.Group()
pulya_gr = pygame.sprite.Group()
rabot = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
in_game = False
verx = False
vniz = False
rs = False

fon_game = Fon(fon, 1)
zastavka = Fon(zastav, 2)
kn = Knopka(zastav)

while running:
    zastav.draw(screen)
    zast(rs)
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
            pygame.mixer.music.rewind()
            pygame.mixer.music.play(-1)
            if not group:
                oxot = Oxotnik(group)
    if in_game:
        fon.draw(screen)
        group.draw(screen)
        pulya_gr.draw(screen)
        pulya_gr.update()
        rabot.update()
        rabot.draw(screen)
        countt()
        if 100 - 10 * count_kill > 40:
            q = 100 - 10 * count_kill
        else:
            q = 40
        if count > q:
            load_robot()
            count = 0
        else:
            count += 1
        if verx:
            oxot.rect.y -= (2 + count_kill * 2)
        if vniz:
            oxot.rect.y += (2 + count_kill * 2)
        kd_pulya += 1
    pygame.display.flip()
    pygame.time.Clock().tick(50)
pygame.quit()