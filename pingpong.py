from pygame import *
from random import *
from time import time as timer
win = display.set_mode((700,500))
win.fill((255,207,171))
display.set_caption('pygame widnow')
game=True
clock=time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,speed,weight,height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(weight,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def show(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x  >5:
            self.rect.x  -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x  < 650:
            self.rect.x += self.speed

while game:
    for e in event.get():
        if e.type==QUIT:
            game = False

    display.update()
    clock.tick(60)