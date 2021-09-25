class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]
# 全局控制类
# 游戏进行时回合控制等
# 此类使用单例模式，只允许存在一个此类的对象
@Singleton
class Global:
    def __init__(self) -> None:
        pass