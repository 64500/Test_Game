# HYM740

from Debug import Debug

# 玩家类
class Player:
    def __init__(self):
        self._anxious=0 #焦虑值
        self._resources=0 #资源值
        self._healthy=100 #健康值
        self._intelligence=10 #智力值
        self._run=5 #行动力
        self.onCreate()
    
    @property
    def anxious(self):
        return self._anxious

    @anxious.setter
    def anxious(self,value):
        if value < 0:
            value = 0
        self._anxious=value
        self.onValueUpdate()

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self,value):
        self._resources=value
        self.onValueUpdate()

    @property
    def healthy(self):
        return self._healthy

    @healthy.setter
    def healthy(self,value):
        if value < 0:
            value = 0
        self._healthy=value
        self.onValueUpdate()

    @property
    def intelligence(self):
        return self._intelligence
        
    @intelligence.setter
    def intelligence(self,value):
        self._intelligence=value
        self.onValueUpdate()

    @property
    def run(self):
        return self._run
        
    @run.setter
    def run(self,value):
        self._run=value
        self.onValueUpdate()

    def kill(self):
        pass;

    # 生命周期方法 对象创建时调用
    def onCreate(self):
        Debug.infoLevel("玩家已创建")

    # 生命周期方法 数值更新时调用
    def onValueUpdate(self):
        if self.anxious >= 100 | self.healthy <=0:
            self.kill()
            
    # 生命周期方法 玩家死亡时调用
    def onDeath(self):
        pass
    # 生命周期方法 对象销毁时调用
    def onDestory(self):
        Debug.infoLevel("玩家已销毁")