import pygame
class Ship:
    '''管理飞船的类'''
    def __init__(self, ai_game): #实例形参 调用游戏资源
        '''初始化飞船并设置初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()#访问屏幕属性 将飞船放到正确位置
        self.settings = ai_game.settings #初始化飞船速度

        #加载飞船图像并获取外接矩形
        # rect矩形对象 pygame处理所有图像都视为矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #每艘新飞船都放在屏幕底部中央
        self.rect.midbottom=self.screen_rect.midbottom
        #双轨路1 虚拟移动测算 存储小数值
        self.x = float(self.rect.x) #初始化位置为600.0 小数点形式
        #移动标志为假
        self.moving_right = False
        self.moving_left = False

    def update_position(self):
        #更新虚拟移动距离 不是实际rect.x
        #限制飞船右移的最大距离为屏幕右边框
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        #限制飞船右移的最大距离为屏幕左边框 因为默认坐标左上角为0所以大于0就不算出界
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #根据虚拟距离测算更新真实的rect.x
        self.rect.x=self.x

    def blit_me(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在底部中央'''
        self.rect.midbottom=self.screen_rect.midbottom
        self.x = float(self.rect.x)