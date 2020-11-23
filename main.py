import pygame
from pygame.locals import *

'''
1:实现飞机的显示，并且可以控制飞机的移动（面向对象）
'''
class HeroPlane(object):
    def __init__(self,screen): #主窗体对象
        '''
        初始化属性
        '''
        self.x = 150
        self.y = 450
        #设置要显示内容的窗口
        self.screen = screen
        #生成飞机的图片对象
        self.imageName = './venv/Include/飞机图标.png'
        self.image = pygame.image.load(self.imageName)
        pass
    def moveleft(self): #向左移动
        if self.x > 0:
            self.x -= 10
        pass
    def moveright(self): #向右移动
        if self.x < 310:
            self.x += 10
        pass
    def display(self): #窗口显示飞机
        self.screen.blit(self.image,(self.x,self.y))
        pass

'''
创建子弹类
'''
class Bullet(object):
    def __init__(self):
        pass
    def display(self):
        pass

def key_control(HeroObj): #定义普通函数监测键盘
    # 获取键盘事件
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出!')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('LEFT!')
                HeroObj.moveleft()#调用函数实现左移动
            elif event.key == K_d or event.key == K_RIGHT:
                print('RIGHT!')
                HeroObj.moveright()#调用函数实现由移动
            elif event.key == K_SPACE:
                print('按下了空格键')

def main():
    #首先创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((350,500),depth=32)
    #设定一个背景图片
    background = pygame.image.load('./venv/Include/背景图.png')

    #添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./venv/Include/背景音乐.MP3')
    pygame.mixer.music.set_volume((0.2))#设置音量
    pygame.mixer.music.play(-1)#循环次数，-1表示无限循环

    #创建一个飞机对象
    hero = HeroPlane(screen)
    #设置一个title
    pygame.display.set_caption('阶段总结-飞机游戏')
    while True:
        screen.blit(background,(0,0)) #调用此方法显示背景图片
        hero.display() #显示玩家飞机的图标
        #获取键盘事件
        key_control(hero)
        pygame.display.update() #刷新背景图

if __name__ == '__main__':
    main()