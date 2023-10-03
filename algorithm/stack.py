class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, v):
        self.stack.append(v)

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack is empty')
        return self.stack.pop()
    
    def __repr__(self):
        return 'stack: ' + str(self.stack)
