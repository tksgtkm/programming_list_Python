class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # コンストラクタに渡されたリストのエイリアスを作成してしまっている
            self.passengers = passengers
            # passengersのリストのコピーを作成すると防げる
            # self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
# バスケットボールチームのメンバーがバスに乗る
bus = TwilightBus(basketball_team)
# チームのメンバーが何人か降りていく
bus.drop('Tina')
bus.drop('Pat')
# バスケットボールチームのメンバーが減っている
print(basketball_team)
# ['Sue', 'Maya', 'Diana']

