"""
$ python3 tools/visitor_replace.py system/filetools2 system system2
List only?y
Visited 18 files
Found 2 files:
system/filetools2/split.py
system/filetools2/join.py

$ python3 tools/visitor_replace.py system/filetools2 system system2
List only?n
Proceed with change?y
Visited 18 files
Changed 2 files:
system/filetools2/split.py
system/filetools2/join.py


"""
import sys
from visitor import SearchVisitor

class ReplaceVisitor(SearchVisitor):

    def __init__(self, fromStr, toStr, listOnly=False, trace=0):
        self.changed = []
        self.toStr = toStr
        self.listOnly = listOnly
        SearchVisitor.__init__(self, fromStr, trace)

    def visitmatch(self, fname, text):
        self.changed.append(fname)
        if not self.listOnly:
            fromStr, toStr = self.context, self.toStr
            text = text.replace(fromStr, toStr)
            open(fname, 'w').write(text)

if __name__ == '__main__':
    listonly = input('List only?') == 'y'
    visitor = ReplaceVisitor(sys.argv[2], sys.argv[3], listonly)
    if listonly or input('Proceed with change?') == 'y':
        visitor.run(startDir=sys.argv[1])
        action = 'Changed' if not listonly else 'Found'
        print('Visited %d files' % visitor.fcount)
        print(action, '%d files:' % len(visitor.changed))
        for fname in visitor.changed:
            print(fname)