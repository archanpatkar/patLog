import time

class LoggerStrategy:
   def __init__(self):
       pass

   def getTime(self):
       return time.asctime(time.localtime(time.time()))

class Logger:
   def __init__(self,strategy):
       self.strategy = strategy;

   def log(self,type,string):
       self.strategy.log(type,string)


class Console(LoggerStrategy):
   def __init__(self):
       LoggerStrategy.__init__(self)
       pass

   def log(self,type,string):
       print("{} {} {} \n".format(super(Console,self).getTime(),type,string));


class File(LoggerStrategy):
   def __init__(self,file):
       LoggerStrategy.__init__(self)
       self.file = open(file,mode='a')

   def log(self,type,string):
       self.file.write("{} {} {} \n".format(super(File,self).getTime(),type,string));
