import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""
    
    @abc.abstractmethod
    def pick(self):
        """
        Remove item at random, returning it.
        This method should raise `LookupError` when the instance is empty
        """

    def loaded(self):
        return bool(self.inspect())
    
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))