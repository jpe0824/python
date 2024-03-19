from abc import ABC, abstractmethod
from typing import Callable
class Iterator(ABC):
    @abstractmethod
    def first(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def current(self):
        pass
class Iterable(ABC):
    @abstractmethod
    def get_iterator(self) -> Iterator:
        pass
class Sequence(ABC):
    @abstractmethod
    def add(self, value):
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def capacity(self) -> int:
        pass

    @abstractmethod
    def get(self, index: int):
        pass
class IterableSequence(Sequence, Iterable, ABC):
    pass
class MyArray(IterableSequence):
    def __init__(self, capacity: int):
        self._array = [None] * capacity
        self._size = 0

    def add(self, value):
        if self._size < len(self._array):
            self._array[self._size] = value
            self._size += 1

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return len(self._array)

    def get(self, index: int):
        return self._array[index]

    def get_iterator(self) -> Iterator:
        return MyIterator(self._array)

class MyIterator(Iterator):
    def __init__(self, array):
        self._array = array
        self._index = 0

    def first(self):
        self._index = 0

    def next(self):
        self._index += 1

    def is_done(self) -> bool:
        return self._index >= len(self._array)

    def current(self):
        return self._array[self._index]

class FilterIterator(Iterator):
    def __init__(self, iterator: Iterator, predicate: Callable):
        self._iterator = iterator
        self._predicate = predicate
        self.first()

    def first(self):
        self._iterator.first()
        self._skip_to_next_valid()

    def next(self):
        self._iterator.next()
        self._skip_to_next_valid()

    def is_done(self) -> bool:
        return self._iterator.is_done()

    def current(self):
        return self._iterator.current()

    def _skip_to_next_valid(self):
        while not self._iterator.is_done() and not self._predicate(self._iterator.current()):
            self._iterator.next()

class ReverseIterator(Iterator):
    def __init__(self, iterator: Iterator):
        self._stack = []
        while not iterator.is_done():
            self._stack.append(iterator.current())
            iterator.next()

    def first(self):
        pass  # Not needed for this iterator

    def next(self):
        self._stack.pop()

    def is_done(self) -> bool:
        return len(self._stack) == 0

    def current(self):
        return self._stack[-1]