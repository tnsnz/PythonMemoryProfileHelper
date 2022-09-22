import os.path

from MemoryProfileHelper import MemoryProfileHelper
from guppy import hpy


class GuppyMemoryProfile(MemoryProfileHelper):
    DUMP_FOLDER_NAME = "/guppyDump"

    def __init__(self, interval=60000, printContents=True):
        super(GuppyMemoryProfile, self).__init__(interval, printContents)
        self.hpy = hpy()

    def process(self):
        heap = self.hpy.heap()
        contents = str(heap)
        self.ioManager.makeDumpFile(os.path.abspath(os.curdir) + self.DUMP_FOLDER_NAME, contents)