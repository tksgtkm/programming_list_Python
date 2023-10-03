from circular_buffer import CircularBuffer

class MovingAverage(CircularBuffer):

    def __init__(self, size):
        CircularBuffer.__init__(self, size)
        self.total = 0

    def getAverage(self):
        if self.count == 0:
            return 0
        return self.total / self.count
    
    def remove(self):
        removed = CircularBuffer.remove(self)
        self.total -= removed
        return removed
    
    def add(self, value):
        if self.isFull():
            self.total -= self.buffer[self.low]
        
        self.total += value
        CircularBuffer.add(self, value)

    def __repr__(self):
        if self.isEmpty():
            return 'ma:[]'
        
        return 'ma:[' + ','.join(map(str, self)) + ']:' + str(self.getAverage())