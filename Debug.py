# HYM740
# 调试用工具类
# 通过设置 Debug.printControl 属性值来控制 Debug 信息是否输出到控制台
# 具体级别为 DEBUG INFO WARN ERROR
class Debug:
    debugLevel="DEBUG"
    debugValue=0

    infoLevel="INFO"
    infoValue=400

    warnLevel="WARN"
    warnValue=500

    errorLevel="ERROR"
    errorValue=700
    
    printControl=400
    # 输出日志，低于设定级别的消息将会被丢弃
    def printlog(message,value):
        if value>Debug.printControl:
            print(message)
    # 自定义消息权重的输出日志
    # message 消息字符串
    # value 消息权重
    def log(message,value):
        Debug.printlog(message,value)
    # DEBUG消息的输出日志
    # message 消息字符串
    def debug(message):
        Debug.printlog("[DEBUG]"+message,Debug.debugValue)
    # INFO消息的输出日志
    # message 消息字符串
    def info(message):
        Debug.printlog("[INFO]"+message,Debug.infoValue)
    # WARN消息的输出日志
    # message 消息字符串
    def warn(message):
        Debug.printlog("[WARN]"+message,Debug.warnValue)
    # ERROR消息的输出日志
    # message 消息字符串
    def error(message):
        Debug.printlog("[ERROR]"+message,Debug.errorValue)