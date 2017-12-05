from patlog.Logger import Logger
from patlog.Logger import Console
from patlog.Logger import File

class LogFactory:
    @staticmethod
    def getConsoleLogger():
        return Logger(Console());

    @staticmethod
    def getFileLogger(file):
        return Logger(File(file));

    @staticmethod
    def getLogger(strategy = Console()):
        return Logger(strategy);
