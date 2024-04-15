import utils
from utils import rf
from containsGAGA import containsGAGA

shortString = 'CTGAGAC'
print('short string result: ', containsGAGA(shortString))
longString = rf('geneticString.txt')
print('long string result: ', containsGAGA(longString))