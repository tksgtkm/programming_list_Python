"""
$ python3 search_all.py . mimetypes
1 => ./search_all.py
2 => ./find.py
3 => ./__init__.py
4 => ./cleanpyc.py
5 => ./cleanpyc-find-shell.py
Found in 0 files, visited 5
"""

import os
import sys
listonly = False
texttexts = ['.py', '.pyw', '.txt', '.c', '.h']

def searcher(startdir, searchkey):
    global fcount, vcount
    fcount = vcount = 0
    for (thisDir, dirsHere, filesHere) in os.walk(startdir):
        for fname in filesHere:
            fpath = os.path.join(thisDir, fname)
            visitfile(fpath, searchkey)

def visitfile(fpath, searchkey):
    global fcount, vcount
    print(vcount+1, '=>', fpath)
    try:
        if not listonly:
            if os.path.splitext(fpath)[1] not in texttexts:
                print('Skipping', fpath)
            elif searchkey in open(fpath).read():
                input('%s has %s' % (fpath, searchkey))
                fcount += 1
    except:
        print('Failed:', fpath, sys.exc_info()[0])
    vcount += 1

if __name__ == '__main__':
    searcher(sys.argv[1], sys.argv[2])
    print('Found in %d files, visited %d' % (fcount, vcount))