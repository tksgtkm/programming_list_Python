from collections import deque
from queue import LifoQueue

list_stack = []
deque_stack = deque()
lifo_stack = LifoQueue()

list_stack.append(27)
print(list_stack.pop())

deque_stack.append(27)
print(deque_stack.pop())

lifo_stack.put(27)
print(lifo_stack.get())

list_stack.append(3)
list_stack.append(4)
list_stack.append(5)
list_stack.append(6)

print(list_stack)