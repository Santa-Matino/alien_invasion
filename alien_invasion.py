#创建pygame窗口
import sys #退出游戏

import pygame

class AlienInvasion():
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init() #初始化背景设置 让python正确工作

        self.screan=pygame.display.set_mode((1200,800))
        #创建显示整个游戏的窗口surface 激活后每次循环自动重绘  尺寸元组
        # 赋给属性screen的对象是一个surface surface理解为是画布或贴纸
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            for event in pygame.event.get(): #函数返回一个列表 所有事件导致循环发生
                #监视键盘和鼠标事件
                # 事件是用户玩游戏的操作 如按键 移动鼠标
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip() #更新屏幕
if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()
