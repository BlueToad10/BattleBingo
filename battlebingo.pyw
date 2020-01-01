import pygame, sys, time, os
from pygame.locals import *
from terminate import *
from waitForPlayerToPressKey import *

Version = "1.0"
WINDOWSIZE = (480, 480)
BACKGROUNDCOLOUR = (0, 255, 0)
LEFT = 1
RIGHT = 3

pygame.init()
pygame.mixer.init()
pygame.display.set_caption(Version)
windowSurface = pygame.display.set_mode(WINDOWSIZE)
icon = pygame.image.load("iconImage.png")
pygame.display.set_icon(icon)

main_list = pygame.sprite.Group()
select_list = pygame.sprite.Group()

Images=[]
for object in sorted(os.listdir("images"), key=len):
    Images.append(pygame.transform.scale(pygame.image.load("images\\" + object), (96, 96)))

selectImage = Images[2]

class window(pygame.sprite.Sprite):
    def __init__(self, imageType, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageType
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 2
    def counterLoop(self, top):
        if self.counter > top:
            self.counter = 0
        elif self.counter < 0:
            self.counter = top
    def rightbutton(self):
        if pygame.sprite.spritecollideany(self, select_list):
            self.counter += 1
            self.counterLoop(2)
            self.image = Images[self.counter]
    def leftbutton(self):
        if pygame.sprite.spritecollideany(self, select_list):
            self.counter -= 1
            self.counterLoop(2)
            self.image = Images[self.counter]

class select(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(selectImage, (1, 1))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

def controls():
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            select_list.update(event.pos[0], event.pos[1])
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == LEFT:
                for object in main_list:
                    object.leftbutton()
            if event.button == RIGHT:
                for object in main_list:
                    object.rightbutton()
        if event.type == QUIT:
            terminate()

def mainLoop():
    windowSurface.fill(BACKGROUNDCOLOUR)
    controls()
    main_list.draw(windowSurface)
    select_list.draw(windowSurface)
    pygame.display.update()

b1i = window(Images[2], 0, 0)
b2i = window(Images[2], 0, 96)
b3i = window(Images[2], 0, 192)
b4i = window(Images[2], 0, 288)
b5i = window(Images[2], 0, 384)

i1i = window(Images[2], 96, 0)
i2i = window(Images[2], 96, 96)
i3i = window(Images[2], 96, 192)
i4i = window(Images[2], 96, 288)
i5i = window(Images[2], 96, 384)

n1i = window(Images[2], 192, 0)
n2i = window(Images[2], 192, 96)
n3i = window(Images[2], 192, 192)
n4i = window(Images[2], 192, 288)
n5i = window(Images[2], 192, 384)

g1i = window(Images[2], 288, 0)
g2i = window(Images[2], 288, 96)
g3i = window(Images[2], 288, 192)
g4i = window(Images[2], 288, 288)
g5i = window(Images[2], 288, 384)

o1i = window(Images[2], 384, 0)
o2i = window(Images[2], 384, 96)
o3i = window(Images[2], 384, 192)
o4i = window(Images[2], 384, 288)
o5i = window(Images[2], 384, 384)

main_list.add(b1i)
main_list.add(b2i)
main_list.add(b3i)
main_list.add(b4i)
main_list.add(b5i)

main_list.add(i1i)
main_list.add(i2i)
main_list.add(i3i)
main_list.add(i4i)
main_list.add(i5i)

main_list.add(n1i)
main_list.add(n2i)
main_list.add(n3i)
main_list.add(n4i)
main_list.add(n5i)

main_list.add(g1i)
main_list.add(g2i)
main_list.add(g3i)
main_list.add(g4i)
main_list.add(g5i)

main_list.add(o1i)
main_list.add(o2i)
main_list.add(o3i)
main_list.add(o4i)
main_list.add(o5i)

select_list.add(select())
while True:
    mainLoop()
