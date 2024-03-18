class Iterator:
    pass

class Iterable:
    pass

class Sequence:
    pass

class IterableSequence(Iterable, Sequence):
    pass

class MyArray(IterableSequence):
    pass

class MyIterator(Iterator):
    pass

class MyFilterIterator(Iterator):
    pass