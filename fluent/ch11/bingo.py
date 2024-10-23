import random

from tombola import Tombola

# BingoCageクラスはTombolaを明示的に継承する
class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        # 初期化時のロードを.load()メソッドにデリゲートする
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        # SystemRandomインスタンスの.shuffle()メソッドを使用する
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick up empty BingoCage')
        
    def __call__(self):
        self.pick()