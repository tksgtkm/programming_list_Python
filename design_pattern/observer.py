import datetime
import itertools
import sys
import time

def main():
    historyView = HistoryView()
    liveView = LiveView()
    model = SliderModel(0, 0, 40)
    model.observers_add(historyView, liveView)
    for value in (7, 23, 37):
        model.value = value
    for value, timestamp in historyView.data:
        print("{:3} {}".format(value, datetime.datetime.fromtimestamp(timestamp)), file=sys.stderr)


class Observed:

    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)

class SliderModel(Observed):

    def __init__(self, minimum, value, maximum):
        super().__init__()
        self.__minimum = self.__value = self.__maximum = None
        self.minimum = minimum
        self.value = value
        self.maximum = maximum

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if self.__value != value:
            self.__value = value
            self.observers_notify()

    @property
    def minimum(self):
        return self.__minimum
    
    @minimum.setter
    def minimum(self, value):
        if self.__minimum != value:
            self.__minimum = value
            self.observers_notify()

    @property
    def maximum(self):
        return self.__maximum
    
    @maximum.setter
    def maximum(self, value):
        if self.__maximum != value:
            self.__maximum = value
            self.observers_notify()

class HistoryView:

    def __init__(self):
        self.data = []

    def update(self, model):
        self.data.append((model.value, time.time()))

class LiveView:

    def __init__(self, length=40):
        self.length = length

    def update(self, model):
        tippingPoint = round(model.value * self.length / (model.maximum - model.minimum))
        td = '<td style="background-color: {}">&nbsp;</td>'
        html = ['<table style="font-family: monospace" border="0"><tr>']
        html.extend(td.format("darkblue") * tippingPoint)
        html.extend(td.format("cyan") * (self.length - tippingPoint))
        html.append("<td>{}</td></tr></table>".format(model.value))
        print("".join(html))

if __name__ == "__main__":
    main()
