# classmethodとstaticmethod

class Demo:
    @classmethod
    def klassmeth(*args):
        # klassmethは位置引数をすべて返すだけの関数
        return args
    @staticmethod
    def statmeth(*args):
        # statmethも同様
        return args
    
# 引数に何を指定しても、Demo.klassmethはDemoクラスを第一引数として受け取る
print(Demo.klassmeth())
# (<class '__main__.Demo'>,)

print(Demo.klassmeth('spam'))
# (<class '__main__.Demo'>, 'spam')

# Demo.statmethはごく普通のシンプルな関数として振る舞う
print(Demo.statmeth())
# ()

print(Demo.statmeth('spam'))
# ('spam',)

# 出力フォーマット

"""
組み込み関数format()及びstr.format()メソッドは実際のフォーマット作業をそれぞれの型について
呼び出した、.__format__(format_spec)メソッドにデリゲートする

ここでformat_specの書式指定子は
・format(my_obj, format_spec)の第二引数
・str.format()で用いられる書式文字列にある{}でくくられた置換フィールドにおいて、
  :以降に置かれたものすべて
"""

brl = 1/2.43
print(brl)

# 書式指定子は0.4f
print(format(brl, '0.4f'))

# 書式指定子は0.2f
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

# クラス属性の上書き

from vector2d_v0 import Vector2d

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
# b'd\x9a\x99\x99\x99\x99\x99\xf1?\x9a\x99\x99\x99\x99\x99\x01@'

# デフォルトではbytesで表現されたときの長さは17バイト
print(len(dumpd))
# 17

# v1インスタンスのtypecodeに「f」をセットする
v1.typecode = 'f'
dumpf = bytes(v1)
print(dumpf)
# b'f\xcd\xcc\x8c?\xcd\xcc\x0c@'

# bytesのダンプの長さは9バイトになった
print(len(dumpf))
# 9

# Vector2d.typecodeは変更されない
# typecodeに「f」を使っているのはv1インスタンスだけ
print(Vector2d.typecode)
# d

"""
クラス属性はパブリックなので、サブクラスが継承する
クラスのデータ属性をカスタマイズするためだけにサブクラス化が行われる。
Djangoのクラスベースビューはこのテクニックを使う
"""

from vector2d_v0 import Vector2d

# クラス属性のtypecodeを上書きするためだけに、ShortVector2dをVector2dのサブクラスとして作成する
class ShortVector2d(Vector2d):
    typecode = 'f'

# テスト用にShortVector2dのインスタンスsvを作成する
sv = ShortVector2d(1/11, 1/27)

# svのreprを確認する
print(sv)
# (0.09090909090909091, 0.037037037037037035)

# bytes表現のバイト長が、17ではなく9になっている
print(len(bytes(sv)))
# 9