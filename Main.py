# HYM740
# 程序入口
# 程序的加载，运行，结束，退出在这个文件中统一管理
# 导入模块
import yaml
from Debug import Debug
if __name__ == '__main__':
  pass
# 加载
def onLoad():
  # 读取config文件夹下的配置文件
    # 配置文件加载顺序
    # 版本号，文本，角色，事件，数据
    # 成功读取版本号后即可使用 Debug 类来执行消息输出

  # 读取版本号后对 Debug 类设置的代码
  Debug.info("正在读取文本")
  # 读取文本的相关代码
  Debug.info("正在读取角色")
  Debug.info("正在读取事件")
  Debug.info("正在读取数据")
  # 初始化类和对象
  # 加载窗体

# 结束
def onFinish():
  pass
# 退出
def onExit():
  pass