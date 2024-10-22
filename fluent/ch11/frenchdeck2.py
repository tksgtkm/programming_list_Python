# カードのシーケンスとしてのトランプの組

import collections

Card = collections.namedtuple('Card', ['rank', 'sult'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'speades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    # シャッフルできるようにするために必要な__setitem__だけ
    def __setitem__(self, position, value):
        self._cards[position] = value

    # MutableSequenceからサブクラス化するには、抽象基底クラスの抽象メソッド
    # __delitem__を実装することが強制される
    def __delitem__(self, position):
        del self._cards[position]

    # MutableSequenceの3つめの抽象メソッドinsertも実装する必要がある
    def insert(self, position, value):
        self._cards.insert(position, value)