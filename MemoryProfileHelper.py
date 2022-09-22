import os
from time import gmtime, strftime

from PyQt5.QtCore import QTimer
from Singleton import Singleton


class ProfileIOManager(metaclass=Singleton):
    def __init__(self, printContents=True):
        self.printContents = printContents

    def makeFolderIfNotExist(self, dir):
        try:
            if not os.path.exists(dir):
                os.makedirs(dir)
        except OSError:
            print('Error: Creating directory. ' + dir)

    def makeDumpFile(self, dir: str, contents: str, fileName=None):
        if (self.printContents):
            print(contents)

        self.makeFolderIfNotExist(dir)

        fileName = "dump_" + strftime(
            "%Y-%m-%d_%H-%M-%S", gmtime()) + ".txt" if None == fileName else fileName
        filePath = dir + "/" + fileName

        f = open(filePath, 'w')
        f.write(contents)
        f.close()


class MemoryProfileHelper():
    def __init__(self, interval=6000, printContents=True):
        self.timer = QTimer()
        self.timer.start(interval)
        self.timer.timeout.connect(self.process)

        self.ioManager = ProfileIOManager(printContents)

    def process(self):
        pass
