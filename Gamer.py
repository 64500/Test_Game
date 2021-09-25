class Gamer:
    # 创建玩家类
    anxious = 0
    # 初始焦虑值
    resources = 0
    # 初始资源点
    healthy = 100
    # 初始健康值
    intelligence = 10
    # 初始智力点

    def __init__(self, name, ):
        pass

    def die(self):
        # 玩家的healthy（健康）值归零 或anxious（焦虑）值达到 100 时死亡
        if Gamer.anxious >= 100:
            pass


class QuanShi(Gamer):
    intelligence = 4
    resources = 5

    def ciaMoney(self):
        QuanShi.resources = QuanShi.resources + 8
        # 拳师使用技能CIA补贴，获得八个资源点


class TianLongRen(Gamer):
    resources = 50


class HaiGui(Gamer):
    resources = 20
    intelligence = 8


class WangYiYun(Gamer):
    resources = 2
    intelligence = 8


class TaTa(Gamer):
    resources = 5
    intelligence = 14


class ZuoTiJia(Gamer):
    resources = 5
    intelligence = 18


class ZhuanXianZong(Gamer):
    resources = 5
    intelligence = 10


class HanHuang(Gamer):
    resources = 5
    intelligence = 6


class GeMingDang(Gamer):
    resources = 8
    intelligence = 14


class MaNon(Gamer):
    resources = 10
    intelligence = 15


class LSP(Gamer):
    resources = 5
    intelligence = 10


class TuMuGou(Gamer):
    resources = 8
    intelligence = 15


class GongZhi(Gamer):
    resources = 50
    intelligence = 4


class TangPing(Gamer):
    resources = 0
    intelligence = 10


class SheChu(Gamer):
    resources = 5
    intelligence = 12


class TwoWorld(Gamer):
    resources = 5
    intelligence = 10


class XPi(Gamer):
    resources = 5
    intelligence = 8


class LPL(Gamer):
    resources = 5
    intelligence = 10


