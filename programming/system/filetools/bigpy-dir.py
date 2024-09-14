import os
import glob
import sys

dirname = '/usr/lib/python3.8'

allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
print(allpy)
for filename in allpy:
    filesizes = os.path.getsize(filename)
    allsizes.append((filesizes, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])