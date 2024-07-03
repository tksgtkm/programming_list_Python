import abc
import sys

def main():
    pencil = SimpleItem("Pencil", 0.40)
    ruler = SimpleItem("Ruler", 1.60)
    eraser = SimpleItem("Eraser", 0.20)
    pencilSet = CompositItem("Pencil Set", pencil, ruler, eraser)
    box = SimpleItem("Box", 1.00)
    boxPencilSet = CompositItem("Boxed Pencil Set", box, pencilSet)
    boxPencilSet.add(pencil)
    for item in (pencil, ruler, eraser, pencilSet, boxPencilSet):
        item.print()

# すべてのアイテムに抽象クラスを持たせる
class AbstractItem(metaclass=abc.ABCMeta):

    @property
    def composite(self):
        pass

    # すべてのクラスをイテラブルに扱う
    def __iter__(self):
        return iter([])
    
# AbstractItemクラスを継承している
# そのためすべての抽象メソッドと抽象プロパティを実装しなければいけない(ここではcompositeだけ)
class SimpleItem(AbstractItem):

    def __init__(self, name, price=0.00):
        self.name = name
        self.price = price

    @property
    def composite(self):
        return False
    
    # ネストされたアイテムを適切なインデントとともに出力する
    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name), file=file)

class AbstractCompositeItem(AbstractItem):

    def __init__(self, *items):
        self.children = []
        if items:
            self.add(*items)

    def add(self, first, *items):
        self.children.append(first)
        if items:
            self.children.extend(items)

    def remove(self, item):
        self.children.remove(item)

    def __iter__(self):
        return iter(self.children)

class CompositItem(AbstractCompositeItem):

    def __init__(self, name, *items):
        super().__init__(*items)
        self.name = name

    @property
    def composite(self):
        return True
    
    @property
    def price(self):
        return sum(item.price for item in self)
    
    def print(self, indent="", file=sys.stdout):
        print("{}${:.2f} {}".format(indent, self.price, self.name), file=file)
        for child in self:
            child.print(indent + "    ")
    
if __name__ == "__main__":
    main()