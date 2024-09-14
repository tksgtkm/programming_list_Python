"""
>>> from filters import filter_files
>>> filter_files('hillbillies.txt', str.upper)
>>> print(open('hillbillies.txt.out').read())
*GRANNY
+JETHRO
*ELLY MAY
+"UNCLE JED"

"""

import sys

def filter_files(name, function):
    input = open(name, 'r')
    output = open(name + '.out', 'w')
    for line in input:
        output.write(function(line))
    input.close()
    output.close()

def filter_stream(function):
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        print(function(line), end='')

if __name__ == '__main__':
    filter_stream(lambda line: line)