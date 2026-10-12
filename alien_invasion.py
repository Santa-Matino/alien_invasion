#创建pygame窗口
import sys #退出游戏
import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship

class AlienInvasion():
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init() #初始化背景设置 让python正确工作
        self.settings = Settings()
        #创建setting实例
        self.bg_color=(230,230,230)  #设置背景颜色为浅灰色 RGB 红绿蓝（0，255）
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN) #全屏设置
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        #创建显示整个游戏的窗口surface 激活后每次循环自动重绘  尺寸元组
        # 赋给属性screen的对象是一个surface surface理解为是画布或贴纸
        pygame.display.set_caption('Alien Invasion')
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group() #存储子弹的编组 管理子弹 自动化的列表

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self.ship.update_position() #移动飞船
            self._update_bullets() #管理子弹
            self._update_screen()


    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():  # 函数返回一个列表 所有事件导致循环发生
            # 监视键盘和鼠标事件
            # 事件是用户玩游戏的操作 如按键 移动鼠标
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''响应按键'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        #按Q键退出
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        '''响应松开'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''创建一颗子弹并加入编组中'''
        if len(self.bullets) < self.settings.bullets_allowed:
         new_bullet = Bullet(self)
         self.bullets.add(new_bullet)

    def _update_bullets(self):  #编写并管理子弹
        self.bullets.update()  # 更新子弹位置 跟踪整个编组内的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        '''更新屏幕图像并切换新屏幕'''
        self.screen.fill(self.settings.bg_color)
        # fill方法处理surface 直接收颜色实参 每次循环都重绘屏幕
        self.ship.blit_me()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()  # 更新屏幕

if __name__ == '__main__':
    ai_game = AlienInvasion()
    ai_game.run_game()
