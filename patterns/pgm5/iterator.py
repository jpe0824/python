from abc import ABC, abstractmethod

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

class IterableSequence(Iterable, Sequence):
    pass

class MyArray(IterableSequence):
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def add(self, value):
        if self._size < self._capacity: # Use _size and _capacity directly
            self._data[self._size] = value
            self._size += 1
        else:
            raise Exception("Array is full")

    def get(self, index: int):
        if index < self._size:
            return self._data[index]
        else:
            raise Exception("Index out of range")

    def get_iterator(self) -> Iterator:
        return MyIterator(self)

    def capacity(self):
        return self._capacity

    def size(self):
        return self._size

class MyIterator(Iterator):
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = -1

    def first(self):
        self.index = 0

    def next(self):
        if self.index < self.sequence.size() - 1:
            self.index += 1
        else:
            self.index = self.sequence.size()

    def is_done(self):
        return self.index >= self.sequence.size()

    def current(self):
        if self.index < 0 or self.index >= self.sequence.size():
            raise Exception("No current element")
        return self.sequence.get(self.index)

class FilterIterator(Iterator):
    def __init__(self, iterator, predicate):
        self.iterator = iterator
        self.predicate = predicate
        self.next_item = None
        self.find_next()

    def first(self):
        self.iterator.first()
        self.find_next()

    def next(self):
        self.iterator.next()
        self.find_next()

    def is_done(self):
        return self.next_item is None

    def current(self):
        if self.next_item is None:
            raise Exception("No current element")
        return self.next_item

    def find_next(self):
        while not self.iterator.is_done():
            item = self.iterator.current()
            if self.predicate(item):
                self.next_item = item
                return
            self.iterator.next()
        self.next_item = None

class ReverseIterator(Iterator):
    def __init__(self, iterator):
        self.iterator = iterator
        self.stack = []
        self.fill_stack()

    def first(self):
        self.iterator.first()
        self.fill_stack()

    def next(self):
        if self.stack:
            self.stack.pop()
            self.fill_stack()

    def is_done(self):
        return not self.stack

    def current(self):
        if not self.stack:
            raise Exception("No current element")
        return self.stack[-1]

    def fill_stack(self):
        while not self.iterator.is_done():
            self.stack.append(self.iterator.current())
            self.iterator.next()

def main():
    # Create a MyArray with capacity 5
    my_array = MyArray(5)
    my_array.add(1)
    my_array.add(2)
    my_array.add(3)
    my_array.add(4)
    my_array.add(5)

    # Create a FilterIterator that filters out even numbers
    def is_odd(x):
        return x % 2 != 0

    filter_iterator = FilterIterator(my_array.get_iterator(), is_odd)

    # Demonstrate FilterIterator
    print("Filtered Iterator (Odd Numbers):")
    filter_iterator.first()
    while not filter_iterator.is_done():
        print(filter_iterator.current())
        filter_iterator.next()

    # Demonstrate ReverseIterator
    print("\nReverse Iterator:")
    reverse_iterator = ReverseIterator(my_array.get_iterator())
    reverse_iterator.first()
    while not reverse_iterator.is_done():
        print(reverse_iterator.current())
        reverse_iterator.next()

    # Demonstrate nested FilterIterators
    print("\nNested FilterIterators:")
    def is_greater_than_two(x):
        return x > 2

    nested_filter_iterator = FilterIterator(filter_iterator, is_greater_than_two)
    nested_filter_iterator.first()
    while not nested_filter_iterator.is_done():
        print(nested_filter_iterator.current())
        nested_filter_iterator.next()

    # Demonstrate ReverseIterator with FilterIterator
    print("\nReverseIterator with FilterIterator:")
    reverse_filter_iterator = ReverseIterator(filter_iterator)
    reverse_filter_iterator.first()
    while not reverse_filter_iterator.is_done():
        print(reverse_filter_iterator.current())
        reverse_filter_iterator.next()

if __name__ == "__main__":
    main()