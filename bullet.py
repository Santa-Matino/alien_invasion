import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞船发射子弹的类'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.color = ai_game.settings.bullet_color

        #在0，0处创建一个子弹矩形，再设置正确位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        #存储子弹的小数位置
        self.y = float(self.rect.y)

    def update(self):
        '''向上移动的子弹'''
        #更新子弹小数位置
        self.y -= self.settings.bullet_speed
        #更新子弹的实际位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect )