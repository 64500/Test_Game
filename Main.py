#!/usr/bin/python3
# HYM740
# 程序入口
# 程序的加载，运行，结束，退出在这个文件中统一管理
# 导入模块
from GlobalControl import Global
import util.YAMLLoad
from Debug import Debug
import wx
import Starting
class A:
  pass
# 加载
def onLoad():
  globals = Global()
  print(globals.time)
  # 读取config文件夹下的配置文件
    # 配置文件加载顺序
    # 文本，角色，事件，数据
    # 成功读取版本号后即可使用 Debug 类来执行消息输出

  # 读取版本号后对 Debug 类设置的代码
  Debug.info("正在读取文本")
  globals.text = util.YAMLLoad.getYAMLDataAll("./config/String.yml")
  # 读取文本的相关代码
  Debug.info("正在读取角色")
  globals.character = util.YAMLLoad.getYAMLDataAll("./config/Character.yml")
  Debug.info("正在读取事件")
  globals.event = util.YAMLLoad.getYAMLDataAll("./event/event.yml")
  Debug.info("正在读取数据")
  # 初始化类和对象
  # 加载窗体
def onShowWindow():
  Starting.show()

# 结束
def onFinish():
  pass
# 退出
def onExit():
  pass
if __name__ == '__main__':
  # 读取版本信息
  version=util.YAMLLoad.getYAMLDataAll("./config/Version.yml")
  if version['Version']['Debug'] :
     Debug.printControl=Debug.debugValue
  onLoad()
  onShowWindow()
  