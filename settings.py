#设置模块 存储所有设置
class Settings:
    '''存储所有设置的类'''
    def __init__(self):
     ''''初始化设置'''
     #屏幕设置
     self.screen_width = 1200
     self.screen_height = 800
     self.bg_color = (230, 230, 230)
     self.ship_speed = 1.5 #只要比1大就行
     #rect只能存储整数值 设置一个双轨路行 这个速度设置为距离平均速度 认识到这一点很重要

     #设置子弹的参数
     self.bullet_speed = 1.0
     self.bullet_width = 3
     self.bullet_height = 15
     self.bullet_color = 60, 60, 60
     self.bullets_allowed = 5
