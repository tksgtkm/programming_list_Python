import os
import sys

rundir = sys.argv[1]
findcmd = r'find %s -name "*.pyc" -print' % rundir
print(findcmd)

count = 0
for fileline in os.popen(findcmd):
    count += 1
    print(fileline, end='')

print('Removed %d .pyc files' % count)