import pygame
from pygame.locals import *
import random  # 随机生成一个数据
import time


class HeroPlane(object):
    def __init__(self, screen):
        # 飞机的默认位置
        self.x = 150
        self.y = 450
        # 设置要显示内容的窗口
        self.screen = screen
        # 生成飞机的图片对象
        self.imageName = './feiji/hero.png'
        self.image = pygame.image.load(self.imageName)
        # 用来存放子弹的列表
        self.bulletList = []
        pass

    def moveleft(self):
        if self.x > 0:
            self.x -= 10
        pass

    def moveright(self):
        if self.x < 310:
            self.x += 10
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历一下
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让这个子弹进行移动下次再最示的时候就会看到子弹在修改后的位置
        pass
    # 发射子弹

    def sheBullet(self):
        # 创造一个新的子弹对象
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newBullet)
        pass
    pass

# 创建子弹类


class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x+2
        self.y = y-20
        self.screen = screen
        self.image = pygame.image.load('./feiji/bullet.png')
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        self.y -= 5
        pass
    # 判断子弹是否越界

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False
        pass
    pass


# 创建敌机类
class EnemyPlane:
    def __init__(self, screen):
        # 设置一个默认方向
        self.direction = 'right '
        # 飞机的默认位置
        self.x = 0
        self.y = 0
        # 设置要显示内容的窗口
        self.screen = screen
        self.bulletList = []
        # 生成飞机的图片对象
        self.imageName = './feiji/enemyplane.png'
        self.image = pygame.image.load(self.imageName)
        pass

    def display(self):
        # 显示敌机以及位置信息
        self.screen.blit(self.image, (self.x, self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历一下
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让这个子弹进行移动下次再 最示的时候就会看到子弹在修改后的位置
        pass
        pass

    def sheBullet(self):
        # 敌机发射
        num = random.randint(1, 20)
        if num == 3:
            newBullet = EnemyBullet(self.x, self.y, self.screen)
            self.bulletList.append(newBullet)
        pass

    def move(self):
        # 敌机移动随机进行
        if self.direction == 'right ':
            self.x += 2
            pass
        elif self.direction == 'left':
            self.x -= 2
            pass
        if self.x > 330:
            self.direction = 'left'
            pass
        elif self.x < 0:
            self.direction = 'right '
            pass
    pass

# 创建敌机子弹类


class EnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y+10
        self.screen = screen
        self.image = pygame.image.load('./feiji/enemybullet.png')
        pass
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        pass

    def move(self):
        self.y += 4
        pass
    # 判断子弹是否越界

    def judge(self):
        if self.y > 500:
            return True
        else:
            return False
        pass
    pass


def key_control(HeroObj):
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print("退出")
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print('left')
                HeroObj.moveleft()
                pass
            elif event.type == K_d or event.key == K_RIGHT:
                print('right')
                HeroObj.moveright()
                pass
            elif event.key == K_SPACE:
                print('按下了空格键，发射子弹')
                HeroObj.sheBullet()
    pass


def main():
    # 首先创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((350, 500), depth=32)
    # 设定一个背景图片
    background = pygame.image.load('./feiji/background.png')
    # 设置一个title
    pygame.display.set_caption('阶段总结-飞机小游戏')

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)   # 循环次数: -1表示无限循环

    # 创建一个飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌机的对象
    enemyplane = EnemyPlane(screen)
    # 设定要显示的内容
    while True:
        screen.blit(background, (0, 0))
        # 显示玩家飞机的图片
        hero.display()
        enemyplane.display()  # 显示敌机
        enemyplane.move()  # 敌机移动
        enemyplane.sheBullet()  # 敌机随机发送子弹
        # 获取键盘事件
        key_control(hero)
        # 更新显示内容
        pygame.display.update()
        time.sleep(0.02)
    pass


if __name__ == '__main__':
    main()
