class HauntedBus:
    # 引数passengersが渡されないと、このパラメータはデフォルトの
    # リストオブジェクト(初期状態は空)にバインドされる
    def __init__(self, passengers=[]):
        # self.passengersはpassengersのエイリアスになる
        self.passengers = passengers

    def pick(self, name):
        # remove()あるいはappendメソッドがself.passengersに対して使用されると
        # 関数オブジェクトの属性であるデフォルトリストを変化させる
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
# ['Alice', 'Bill']

bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)
# ['Bill', 'Charlie']

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)
# ['Carrie']

bus3 = HauntedBus()
# デフォルトなのに誰かいる
print(bus3.passengers)
# ['Carrie']
bus3.pick('Dave')
# bus3に乗車したはずのDaveがbus2に乗っている
print(bus2.passengers)
# ['Carrie', 'Dave']
# bus2.passengersとbus3.passengersが同じリストを参照している
print(bus2.passengers is bus3.passengers)
# True
# bus1.passengersのリストは異なる
print(bus1.passengers)
# ['Bill', 'Charlie']

print(dir(HauntedBus.__init__))

print(HauntedBus.__init__.__defaults__)
# (['Carrie', 'Dave'],)

print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)
# True