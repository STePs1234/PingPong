from pygame import *
from random import *
from time import time as timer
win = display.set_mode((700,500))
win.fill((255,207,171))
display.set_caption('pygame widnow')
game=True
clock=time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed, weight, height):
        sprite.Sprite.__init__(self)
        self.image = image.load(player_image).convert_alpha()
        pixels = PixelArray(self.image)
        for y in range(self.image.get_height()):
            for x in range(self.image.get_width()):
                r, g, b, a = self.image.get_at((x, y))
                if 210 <= r <= 255 and 210 <= g <= 255 and 210 <= b <= 255:
                    pixels[x, y] = (0, 0, 0, 0)  # Полная прозрачность
        del pixels
        self.image = transform.scale(self.image, (weight, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def show(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y  >5:
            self.rect.y  -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y  < 350:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y  -= self.speed
        if keys_pressed[K_s] and self.rect.y  < 350:
            self.rect.y += self.speed
ball=GameSprite('ball.png',350,250,10,50,50)
player_l=Player('Tenisl.jpg',15,250,5,150,120)
player_r=Player('Tenisr.jpg',550,250,5,150,120)
font.init()
font=font.Font(None,35)
losel=font.render('PLAYER LEFT LOST',True,(180,0,0))
loser=font.render('PLAYER RIGHT LOST',True,(180,0,0))
finish=False
speed_x=3
speed_y=3
while game:
    for e in event.get():
        if e.type==QUIT:
            game = False
    if finish != True:
        win.fill((255,207,171))

        player_r.show()
        player_l.show()
        player_l.update_l()
        player_r.update_r()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        if sprite.collide_rect(player_l,ball) or sprite.collide_rect(player_r,ball):
            speed_x*=-1
            speed_y*=-1
        if ball.rect.x < 0:
            finish=True
            win.blit(losel,(200,200))
            gameover=True
        if ball.rect.x > 650:
            finish=True
            win.blit(loser,(200,200))
            gameover=True
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *=-1


    
    ball.show()
    display.update()
    clock.tick(60)