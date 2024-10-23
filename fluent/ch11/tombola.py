import abc

# abc.ABCからサブクラス化することで抽象基底クラスを定義する
class Tombola(abc.ABC):

    # 抽象メソッドには@abstractmethodデコレータで印がつけられている
    # たいてい中身はdocstring以外は空
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""
    
    # 取得する要素がないときはLookupErrorを上げるようにdocstringで指示している
    @abc.abstractmethod
    def pick(self):
        """
        Remove item at random, returning it.
        This method should raise `LookupError` when the instance is empty
        """
    # 抽象基底クラスに具象メソッドを含むこともできる
    def loaded(self):
        # 抽象基底クラスの具象メソッドは、抽象基底クラスによって定義されたインターフェースだけに
        # 依存しなければならない
        return bool(self.inspect())
    
    def inspect(self):
        items = []
        # 具象サブクラスがどのように要素を収容しているか知ることはできない。
        # .pick()を連続して呼び出してTombolaを空にすることでinspectの結果を作成できる
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        # while処理で空にしたら、.load()を使ってすべて戻す
        self.load(items)
        return tuple(sorted(items))