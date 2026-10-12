import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        '''初始化外星人并设置其位置'''
        super().__init__()
        self.screen = ai_game.screen

        #加载外星人图像并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初在屏幕左上角出现
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #存储外星人精准水平位置
        self.x=float(self.rect.x)