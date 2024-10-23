# インターフェースプロトコルから抽象基底クラスへ

# 例 11-3 __getitem__だけでシーケンスプロトコルを部分的に実装

class Foo:

    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]
    
f = Foo()
print(f[1])
# 10

for i in f:print(i)
# 0
# 10
# 20

print(20 in f)
# True

print(15 in f)
# False

"""
__iter__メソッドが実装されていないにもかかわらず、Fooインスタンスはイテラブルになっている
__getitem__メソッドがあればPythonはフォールバックとして0で始まる整数のインデックスを用いて
このメソッドを呼び出し、オブジェクトの反復処理を試みる
また、__contains__メソッドがなくてもin演算子を動作させる
"""

# シーケンスプロトコルを用いた実装例はFrenchDeck.pyを参照

# プロトコルをランタイムで実装するモンキーパッチ

# 標準ライブラリの関数random.shuffleの利用例
from random import shuffle
l = list(range(10))
shuffle(l)

print(l)
# [1, 8, 7, 3, 6, 4, 9, 0, 2, 5]

# これをFrenchdeckインスタンスをシャッフルすると例外が発生する
from random import shuffle
from frenchdeck import FrenchDeck

deck = FrenchDeck()
# shuffle(deck)

"""
Traceback (most recent call last):
  File "ch11.py", line 50, in <module>
    print(shuffle(deck))
  File "/usr/lib/python3.8/random.py", line 307, in shuffle
    x[i], x[j] = x[j], x[i]
TypeError: 'FrenchDeck' object does not support item assignment
"""

# __setitem__メソッドを用意してシーケンス可変にもできる
# ランタイムで修正する

# deck, position, cardを引数として取る関数を作成する
def set_card(deck, position, card):
    deck._cards[position] = card

# FrenchDeckクラスの__setitem__と言う名の属性にset_cardを割り当てる
FrenchDeck.__setitem__ = set_card
# 可変なシーケンスプロトコルに必要なメソッドを実装してシャッフルをする
shuffle(deck)
print(deck[:5])
# [Card(rank='10', sult='clubs'), Card(rank='K', sult='clubs'), Card(rank='3', sult='diamonds'), Card(rank='10', sult='diamonds'), Card(rank='5', sult='diamonds')]

"""
set_cardがdeckオブジェクトに_cardsという名前の属性があることを知っており、
_cardsが可変なシーケンスでなければならないところ
そのうえでFrenchDeckクラスの特殊なメソッド__setitem__を関数set_cardにする
ソースコードをいじらずにクラスやモジュールをランタイムで変更することを
モンキーパッチという
"""

"""
ダックタイピング：
オブジェクトの本来の型は無視し、その代わりにオブジェクトを使っていくうえで
必要なメソッドの名前、シグネチャ、セマンティクスの的確な実装に集中するという方法

Pythonならばisinstanceによるオブジェクトの型検査は避けるということになる。

グースタイピング：
clsが抽象基底クラスである限り、isinstance(obj, cls)は問題ないという意味
換言すればclsのメタクラスはabc.ABCMetaということになる。
"""

"""
抽象基底クラスは「シーケンス」や「正確な数値」のような、フレームワークで
導入される非常に一般的な概念や抽象性をカプセル化するためのもの
大抵、新しい抽象基底クラスを書く必要はないし、既存のものを利用するだけで
重大な設計ミスの危険を冒さなくて済む
"""

# 抽象基底クラスのサブクラス化

# frenchdeck2.pyを参照

# 抽象基底クラスの定義と利用

"""
抽象クラスを作成するのは、そのクラスをフレームワークの拡張ポイントとして使うような場合に限る。

Tombola抽象基底クラスには4つのメソッドを用意する

.load() 容器に要素を入れる
.pick() 容器からランダムに要素を一個削除し、それを返す
,loaded() 容器に少なくとも一個の要素があればTrueを返す
.inspect() その時点で容器にある要素から構築したタプルを、その容器を変えることなく 
           ソートした上で返す(内部の順序は保たれない)
"""

# 実装はtombola.pyを参照