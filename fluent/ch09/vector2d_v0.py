from array import array
import math

class Vector2d:
    # typecode(タイプコード)は、Vector2dインスタンスをbytesに、
    # あるいはその逆に変換するときに用いるクラス属性
    typecode = 'd'
    
    # __init__でxとyをfloatに変換しておくと、
    # Vecotr2dが不適切な引数で呼び出されたときに
    # エラーを早い段階でキャッチできる
    def __init__(self, x, y):
        # 属性をプライベートにするにはアンダースコアを２個つける必要がある
        self.__x = float(x)
        self.__y = float(y)

    # @propertyはデコレータで、プロパティのgetterメソッドを修飾する
    @property
    # getterメソッドは外部にアクセスできるパブリックなプロパティ(x)から名付ける
    def x(self):
        # self.__xを返す
        return self.__x
    
    # プロパティyでも同様にする
    @property
    def y(self):
        return self.__y

    # __iter__でVector2dをイテラブルにする。
    # これでx, y = my_vectorのようなアンパックができる
    # ここではジェネレータ式を使って要素を順次生成するという実装にしている
    # パブリックなプロパティをself.xまたはself.yを経由して読み取る
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    # __repr__では、{!r}に要素書き出すことで要素のreprを取得し、文字列を構築する
    # Vector2dはイテラブルなので、*selfは要素のxとyをfloatに引き渡す。
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    # イテラブルなVector2dからなら、順序付けられた組のtupleの表示用に簡単に生成できる
    def __str__(self):
        return str(tuple(self))
    
    # bytesを生成するには、まずタイプコードをbytesに変換する
    # インスタンスを反復処理することでarrayを生成し、それをbytesに変換してから
    # タイプコードから変換したbytesに連結する
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    
    # てっとり早く各要素を比較するには、引数からタプルを作成する
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            # fmt_specのから末尾のpを取り除く
            fmt_spec = fmt_spec[:-1]
            # 書式指定子の末尾が'p'のときはベクトルを極座標形式にするという
            # 書式コードを追加する
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            # 書式末尾がpでなければ直交座標なので、selfのx, y要素を用いる
            coords = self
            outer_fmt = '({}, {})'
        # 組み込み関数のformatを使用してfmt_specをベクトル要素にそれぞれ適用し、
        # フォーマットした文字列のイテラブルを生成する
        components = (format(c, fmt_spec) for c in coords)
        # フォーマットした文字列を式(x, y)に挿入する
        return outer_fmt.format(*components)

    # 別バージョンのコンストラクタ
    # バイナリシーケンスからVector2dを構築するメソッド

    # クラスメソッドはclassmethodデコレータで装飾する
    @classmethod
    # 引数selfはない、そのクラス自体をclsとして指定する
    def frombytes(cls, octets):
        # (引数octets)最初のバイトにあるtypecodeを読み取る
        typecode = chr(octets[0])
        # バイナリシーケンスのoctetsからmemoryviewを作成し、
        # 先のtypecodeを用いてキャストする
        memv = memoryview(octets[1:]).cast(typecode)
        # キャストの結果得られたmemoryviewをアンパックし、
        # コンストラクタに必要な２つの引数にする
        return cls(*memv)
    
v1 = Vector2d(3, 4)
# Vector2dの要素は(getattrメソッドを呼び出さなくても)属性を介して直接アクセスできる
print(v1.x, v1.y)
# 3.0 4.0

# Vector2dは変数のタプルにアンパックされる
x, y = v1
print(x, y)
# 3.0 4.0

# Vector2dのreprはインスタンスを生成したときのソースコードをエミュレートする
print(v1)
# (3.0, 4.0)

# evalを使うと、Vector2dのreprがそのインスタンスを生成したときの
# コンストラクタ呼び出しを忠実に表現している
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
# True

# printはstrを呼び出し、strはVector2dの一組のデータを順に表示する
print(v1)
# (3.0, 4.0)

# bytesは__bytes__メソッドを使ってバイナリ表現を生成する
octets = bytes(v1)
print(octets)
# b'd\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x10@'

# absは__abs__メソッドを使ってVector2dの大きさ(ベクトルの長さ)を返す
print(abs(v1))
# 5.0

# boolは__bool__メソッドを使ってVector2dの大きさが0ならFalseを
# それ以外ならTrueを返す
print(bool(v1), bool(Vector2d(0, 0)))
# True False

v1_clone = Vector2d.frombytes(bytes(v1))
print(v1_clone)
# (3.0, 4.0)

print(v1 == v1_clone)
# True

# クラスで__format__が定義されていなければ、objectから継承されたメソッドが
# str(my_object)を返す。Vector2dには__str__があるので、以下のように動作する

v1 = Vector2d(3, 4)
print(format(v1))

# そして、__format__メソッドを実装して書式指定子を指定できるようにする

print(format(Vector2d(1, 1), 'p'))
# <1.4142135623730951, 0.7853981633974483>

print(format(Vector2d(1, 1), '.3ep'))
# <1.414e+00, 7.854e-01>

print(format(Vector2d(1, 1), '0.5fp'))
# <1.41421, 0.78540>

# ハッシュ可能なVector2d

# Vector2dをハッシュ可能にするには__hash__と__eq__の実装が必要になる
# (__eq__すでに実装している)
# また、Vector2dインスタンスを不変にしなければいけない

v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))
# 7 384307168202284039

print(set([v1, v2]))
# {Vector2d(3.1, 4.2), Vector2d(3.0, 4.0)}