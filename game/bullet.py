# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    """子弹类"""

    def __init__(self, screen, plane, speed):
        self.screen = screen
        super().__init__()
        # 子弹速度
        self.speed = speed or 10
        self.plane = plane

        # 加载子弹的位置
        self.image = pygame.image.load(constants.BULLET_TMG)

        # 改变子弹的位置
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

        # 发射的音效
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_TMG)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, war):
        """"更新子弹位置"""
        self.rect.top -= self.speed
        # 超出屏幕范围
        if self.rect.top <= 0:
            self.remove(self.plane.bullets)
            print(self.plane.bullets)
        # 绘制子弹
        self.screen.blit(self.image, self.rect)
        # 碰撞检测
        rect = pygame.sprite.spritecollide(self, war.enemies, False)
        print(rect, 666)
        for r in rect:
            # 1.子弹消失
            self.kill()
            # 2.飞机爆炸效果
            r.broken_down()
            # 3.统计游戏成绩
            war.rest.score += constants.SCORE_SHOOT_SMALL
            # 保存历史记录
            war.rest.set_history()
