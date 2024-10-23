import random

from tombola import Tombola

class LotteryBlower(Tombola):

    def __init__(self, iterable):
        # イニシャライザはイテラブルなら何でも引数で受け付け、これからリストを作成する
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            # 関数random.randrangeは指定されたリストが空のときValueErrorを上げる
            # Tombolaとの互換性を上げるため、このエラーはとりあえずキャッチしておいて、
            # かわりにLookupErrorを上げる
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LotteryBlower')
        # エラーでなければ、ランダムに選択した要素をself._ballsから取り出す
        return self._balls.pop(position)
    
    # Tombola.loadedはinspectを呼び出しているが、ここではloadedをオーバーライドすることで
    # この呼び出しを回避する。
    # self._ballsを使えば全要素をソートしたタプルにする必要はなく、高速に実行できる
    def loaded(self):
        return bool(self._balls)
    
    # inspectも一行コードでオーバーライドする
    def inspect(self):
        return tuple(sorted(self._balls))