"""
python3 tools/visitor_cpall.py system/filetools filetools3
Copying...
Copied 24 files,  3 directories in 0.01805096600037359 seconds

"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from visitor import FileVisitor
from programming.system.filetools.cpall import copyfile

class CpallVisitor(FileVisitor):

    def __init__(self, fromDir, toDir, trace=True):
        self.fromDirLen = len(fromDir) + 1
        self.toDir = toDir
        FileVisitor.__init__(self, trace=trace)

    def visitdir(self, dirpath):
        toPath = os.path.join(self.toDir, dirpath[self.fromDirLen:])
        if self.trace:
            print('d', dirpath, '=>', toPath)
        os.mkdir(toPath)
        self.dcount += 1

    def visitfile(self, filepath):
        toPath = os.path.join(self.toDir, filepath[self.fromDirLen:])
        if self.trace:
            print('f', filepath, '=>', toPath)
        copyfile(filepath, toPath)
        self.fcount += 1

if __name__ == '__main__':
    import sys
    import time
    fromDir, toDir = sys.argv[1:3]
    trace = len(sys.argv) > 3
    print('Copying...')
    start = time.perf_counter()
    wakler = CpallVisitor(fromDir, toDir, trace)
    wakler.run(startDir=fromDir)
    print('Copied', wakler.fcount, 'files, ', wakler.dcount, 'directories', end=' ')
    print('in', time.perf_counter() - start, 'seconds')