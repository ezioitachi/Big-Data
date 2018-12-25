import pygame

from plane_sprites import *

pygame.init()

screen=pygame.display.set_mode((480,852))

#背景
background=pygame.image.load("./images/background.png")
screen.blit(background,(0,0))


#飞机
hero=pygame.image.load("./images/hero1.png") #png图像支持透明
screen.blit(hero,(200,500))
hero_rect=pygame.Rect(200,500,100,124)

pygame.display.update()

#时间
clock=pygame.time.Clock()


#敌机
enemy=GameSprite("./images/enemy0.png")
enemy1=GameSprite("./images/enemy0.png",2)
enemy_group=pygame.sprite.Group(enemy,enemy1)



while True:
    clock.tick(60)#一秒60帧

    if (hero_rect.y+hero_rect.height)<=0:
        hero_rect.y=852

    hero_rect.y-=5
    screen.blit(background,(0,0))
    screen.blit(hero,hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)





    pygame.display.update()

    for event in pygame.event.get():#事件监听




        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit() #终至目前的全部程序

pygame.quit()
