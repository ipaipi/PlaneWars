# !/usr/bin/eny python3
# -*- coning: utf-8 -*-
__author__ = 'LaoTan'

from game.war import PlaneWar


def main():
    """游戏入口，main方法 """
    war = PlaneWar()
    # 添加小型飞机
    war.add_small_enemies(4)
    war.run_game()


main()
