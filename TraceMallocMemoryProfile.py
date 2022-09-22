import os.path
import tracemalloc

from MemoryProfileHelper import MemoryProfileHelper


class TraceMallocMemoryProfile(MemoryProfileHelper):
    DUMP_FOLDER_NAME = "/dumpTraceMalloc"
    DUMP_FOLDER_NAME_CMP_PREV = "/dumpComparePrev"
    DUMP_FOLDER_NAME_CMP_ORI = "/dumpCompareOrigin"

    def __init__(self, interval=60000, printContents=True):
        super(TraceMallocMemoryProfile, self).__init__(interval, printContents)

        tracemalloc.start()

        self.flag = True

        self.originSnapShot = tracemalloc.take_snapshot()
        self.snapshot1 = None
        self.snapshot2 = None

    def process(self):
        snapshot = tracemalloc.take_snapshot()

        if True == self.flag:
            self.snapshot1 = snapshot
            self.flag = False
        else:
            self.snapshot2 = snapshot
            self.flag = True

            top_stats = self.snapshot2.compare_to(self.snapshot1, 'lineno')

            contents = ""

            print("[ Top 20 differences ]")
            for stat in top_stats[:20]:
                contents += str(stat) + "\n"

            self.ioManager.makeDumpFile(os.path.abspath(os.curdir) + self.DUMP_FOLDER_NAME + self.DUMP_FOLDER_NAME_CMP_PREV,
                              contents)

        top_stats = snapshot.compare_to(self.originSnapShot, 'lineno')

        contents = ""

        print("[ Top 50 differences ]")
        for stat in top_stats[:50]:
            contents += str(stat) + "\n"

        self.ioManager.makeDumpFile(os.path.abspath(os.curdir) + self.DUMP_FOLDER_NAME + self.DUMP_FOLDER_NAME_CMP_ORI, contents)