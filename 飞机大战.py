import pygame
import random
import time
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
        self.imageName = './Include/飞机图标.png'
        self.image = pygame.image.load(self.imageName)
        self.Bulletlist=[]#用来存放子弹的列表
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
        needDelItemList=[] #完善子弹的展示逻辑
        for item in self.Bulletlist:
            if item.judge():
                needDelItemList.append(item)
        for i in needDelItemList: #重新遍历子弹，删除越界的子弹
            self.Bulletlist.remove(i)
        for bullet in self.Bulletlist:
            bullet.display() #显示子弹的位置
            bullet.move() #移动子弹的位置，下次再显示就会看到子弹修改后的位置
        pass
    def sheBullet(self): #发射子弹
        newBullet = Bullet(self.x,self.y,self.screen) #创建一个新的子弹对象
        self.Bulletlist.append(newBullet) #将子弹存放到子弹列表
'''
创建子弹类
'''
class Bullet(object):
    def __init__(self,x,y,screen):
        self.x = x+13
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load('./Include/Bullet.png')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y -= 0.2
        pass
    def judge(self): #判断子弹是否越界
        if self.y<0:
            return True
        else:
            return False

'''
敌方飞机的子弹类
'''
class EnemyBullet(object):
    def __init__(self,x,y,screen):
        self.x = x
        self.y = y+5
        self.screen = screen
        self.image = pygame.image.load('./Include/Bullet1.png')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y += 0.2
        pass
    def judge(self): #判断子弹是否越界
        if self.y>500:
            return True
        else:
            return False

'''
创建敌方飞机
'''
class EnemyPlane(object):
    def __init__(self,screen):
        self.direction = 'right'#默认设置一个移动方向
        self.screen = screen
        self.x = 0
        self.y = 0
        self.screen = screen
        self.BulletList=[]
        self.imageName = './Include/敌方飞机.png'
        self.image = pygame.image.load(self.imageName)
    def display(self): #显示敌方飞机以及子弹位置的信息
        self.screen.blit(self.image,(self.x,self.y))
        needDelItemList = []  # 完善子弹的展示逻辑
        for item in self.BulletList:
            if item.judge():
                needDelItemList.append(item)
        for i in needDelItemList:  # 重新遍历子弹，删除越界的子弹
            self.BulletList.remove(i)
        for bullet in self.BulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 移动子弹的位置，下次再显示就会看到子弹修改后的位置
    def sheBullet(self): #敌方随机发射的子弹
        num = random.randint(1,200)
        if num == 3:
            newBullet = EnemyBullet(self.x,self.y,self.screen)
            self.BulletList.append(newBullet)
        pass
    def move(self): #敌方飞机随机移动
        if self.direction == 'right':
            self.x+=0.1
        elif self.direction =='left':
            self.x-=0.1
        if self.x>330:
            self.direction = 'left'
        elif self.x<0:
            self.direction = 'right'
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
                print('按下了空格键,发射子弹')
                HeroObj.sheBullet()

def main():
    #首先创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((350,500),depth=32)
    #设定一个背景图片
    background = pygame.image.load('./Include/背景图.png')

    #添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./Include/背景音乐.MP3')
    pygame.mixer.music.set_volume((0.2))#设置音量
    pygame.mixer.music.play(-1)#循环次数，-1表示无限循环

    #创建一个飞机对象
    hero = HeroPlane(screen)
    #设置一个title
    pygame.display.set_caption('阶段总结-飞机游戏')
    #创建一个敌方飞机对象
    enemyplane = EnemyPlane(screen)
    while True:
        screen.blit(background,(0,0)) #调用此方法显示背景图片
        hero.display() #显示玩家飞机的图标
        enemyplane.display() #显示敌方飞机的图标
        enemyplane.move() #敌方飞机移动
        enemyplane.sheBullet() #敌方飞机随机发射子弹
        #获取键盘事件
        key_control(hero)
        pygame.display.update() #刷新背景图
        pygame.time.Clock().tick(500)

if __name__ == '__main__':
    main()