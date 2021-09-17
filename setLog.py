import logging
logevelDict={
        "debug" : logging.DEBUG,
        "info" : logging.INFO,
        "warning" : logging.WARNING,
        "error" : logging.ERROR
    }
class Logger:
    def __init__(self,filename,level):
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(logevelDict.get(level))
        format = logging.Formatter('%(asctime)s %(filename)s %(levelname)s [yun] %(message)s')
        sh = logging.StreamHandler() #往屏幕上输出
        sh.setFormatter(format)
        fileOutput = logging.FileHandler(filename,mode='w',encoding="utf-8") #往文件输出
        fileOutput.setFormatter(format)
        self.logger.addHandler(sh)
        self.logger.addHandler(fileOutput)
log = Logger("compare.log","info")
orbError = Logger("orbError.log","error")
