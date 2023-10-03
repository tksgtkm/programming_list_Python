from circular_buffer import CircularBuffer

SIZE = 5

cb = CircularBuffer(SIZE)

print(cb.isEmpty())

cb.add(1)
cb.add(1)
cb.add(2)
cb.add(3)
cb.add(5)

print(cb)

print(cb.isFull())

cb.add(8)
print(cb)

cb.remove()

cb.add(13)
print(cb)