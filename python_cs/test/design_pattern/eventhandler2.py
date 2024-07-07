import sys
import Event
from Qtrack import coroutine

def main():
    print("Handler Chain #1")
    pipeline = key_handler(mouse_handler(timer_handler()))
    while True:
        event = Event.next()
        if event.kind == Event.TERMINATE:
            break
        pipeline.send(event)

    print("\nHandler Chain #2 (debugging)")
    pipeline = debug_handler(pipeline)
    while True:
        event = Event.next()
        if event.kind == Event.TERMINATE:
            break
        pipeline.send(event)

@coroutine
def debug_handler(successor, file=sys.stdout):
    while True:
        event = (yield)
        file.write("DEBUG*: {}\n".format(event))
        successor.send(event)

@coroutine
def mouse_handler(successor=None):
    while True:
        event = (yield)
        if event.kind == Event.MOUSE:
            print("Click:    {}".format(event))
        elif successor is not None:
            successor.send(event)

@coroutine
def key_handler(successor=None):
    while True:
        event = (yield)
        if event.kind == Event.KEYPRESS:
            print("Press:    {}".format(event))
        elif successor is not None:
            successor.send(event)

@coroutine
def timer_handler(successor=None):
    while True:
        event = (yield)
        if event.kind == Event.TIMER:
            print("Timeout:    {}".format(event))
        elif successor is not None:
            successor.send(event)

if __name__ == "__main__":
    main()