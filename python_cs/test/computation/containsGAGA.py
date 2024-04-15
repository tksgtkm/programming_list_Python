import utils
from utils import rf

def containsGAGA(inString):
    if 'GAGA' in inString:
        return 'yes'
    else:
        return 'no'
    
def testContainsGAGA():
    testVals = [('GAGA', 'yes'),
                ('CCCGAGA', 'yes'),
                ('AGAGAGAAGAAGAGAAA', 'yes'),
                ('GAGACCCCC', 'yes'),
                ('', 'no'),
                ('CCCCCCCCGAGTTTT', 'no'),
                ]
    for (inString, solution) in testVals:
        val = containsGAGA(inString)
        utils.tprint(inString, ':', val)
        assert val == solution

