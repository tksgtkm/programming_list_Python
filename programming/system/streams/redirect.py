"""
>>> from io import StringIO
>>> buff = StringIO()
>>> print(42, file=buff)
>>> print('spam', file=buff)
>>> print(buff.getvalue())
42
spam

>>> from redirect import Output
>>> buff = Output()
>>> print(43, file=buff)
>>> print('eggs', file=buff)
>>> print(buff.text)
43
eggs

"""

import sys

class Output:

    def __init__(self):
        self.text = ''
    
    def write(self, string):
        self.text += string
    
    def writelines(self, lines):
        for line in lines:
            self.write(line)

class Input:

    def __init__(self, input=''):
        self.text = input
    
    def read(self, size=None):
        if size == None:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:size], self.text[size:]
        return res
    
    def readline(self):
        eoln = self.text.find('\n')
        if eoln == -1:
            res, self.text = self.text, ''
        else:
            res, self.text = self.text[:eoln+1], self.text[eoln+1:]
        return res
    
def redirect(function, pargs, kwargs, input):
    savestreams = sys.stdin, sys.stdout
    sys.stdin = Input(input)
    sys.stdout = Output()
    try:
        result = function(*pargs, **kwargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams
    return (result, output)