"""
深いコピーとは内包されているオブジェクトの参照を共有しない複製を指す
copyモジュールには任意のオブジェクトの深いコピーを返すdeepcopy関数と
浅いコピーを返すcopy関数がある
"""

class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

import copy

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

# copyとdeepcopyを使ってそれぞれ異なるBusインスタンスを作成する
print(id(bus1), id(bus2), id(bus3))
# 140147218277568 140147216723344 140147216398032

# bu2からも削除される
bus1.drop('Bill')

print(bus2.passengers)
# ['Alice', 'Claire', 'David']

# bus1とbus2が同じリストオブジェクトを共有している
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
# 140371482432512 140371482432512 140371482485312

# bus3は深いコピーなので、passengers属性は別のリストを参照している
print(bus3.passengers)
# ['Alice', 'Bill', 'Claire', 'David']