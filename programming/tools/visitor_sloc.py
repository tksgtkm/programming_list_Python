"""
$ python3 tools/visitor_sloc.py preview/cgi-bin/
preview/cgi-bin/ ...
cgi101.py
peoplecgi.py
Visited 2 files and 1 dirs
--------------------------------------------------------------------------------
Source files=>2, lines=>101
By Types:
{'.c': {'files': 0, 'lines': 0},
 '.cgi': {'files': 0, 'lines': 0},
 '.cxx': {'files': 0, 'lines': 0},
 '.h': {'files': 0, 'lines': 0},
 '.html': {'files': 0, 'lines': 0},
 '.i': {'files': 0, 'lines': 0},
 '.py': {'files': 2, 'lines': 101},
 '.pyw': {'files': 0, 'lines': 0}}

Check sums: 101 2

Python only walk:
{'.py': {'files': 2, 'lines': 101}, '.pyw': {'files': 0, 'lines': 0}}

"""
import os
import sys
import pprint

from visitor import FileVisitor

class LinesByType(FileVisitor):

    srcExts = []

    def __init__(self, trace=1):
        FileVisitor.__init__(self, trace=trace)
        self.srcLines = self.srcFiles = 0
        self.extSums = {
            ext: dict(files=0, lines=0) for ext in self.srcExts
        }

    def visitsource(self, fpath, ext):
        if self.trace > 0:
            print(os.path.basename(fpath))
        lines = len(open(fpath, 'rb').readlines())
        self.srcFiles += 1
        self.srcLines += lines
        self.extSums[ext]['files'] += 1
        self.extSums[ext]['lines'] += lines

    def visitfile(self, filepath):
        FileVisitor.visitfile(self, filepath)
        for ext in self.srcExts:
            if filepath.endswith(ext):
                self.visitsource(filepath, ext)
                break

class PyLines(LinesByType):
    srcExts = ['.py', '.pyw']

class SourceLines(LinesByType):
    srcExts = ['.py', '.pyw', '.cgi', '.html', '.c', '.cxx', '.h', '.i']

if __name__ == '__main__':
    walker = SourceLines()
    walker.run(sys.argv[1])
    print('Visited %d files and %d dirs' % (walker.fcount, walker.dcount))
    print('-'*80)
    print('Source files=>%d, lines=>%d'  % (walker.srcFiles, walker.srcLines))
    print('By Types:')
    pprint.pprint(walker.extSums)

    print('\nCheck sums:', end=' ')
    print(sum(x['lines'] for x in walker.extSums.values()), end=' ')
    print(sum(x['files'] for x in walker.extSums.values()))

    print('\nPython only walk:')
    walker = PyLines(trace=0)
    walker.run(sys.argv[1])
    pprint.pprint(walker.extSums)    