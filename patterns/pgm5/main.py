from iterator import MyArray, FilterIterator, ReverseIterator

def main():
    # 1. With two different types of elements
    print("MyArray with two different types of elements:")
    my_array = MyArray(10)
    my_array.add(1)
    my_array.add(2)
    my_array.add(3)
    my_array.add(4)
    my_array.add(5)
    my_array.add("a")
    my_array.add("b")
    my_array.add("c")
    my_array.add("d")
    my_array.add("e")

    iterator = my_array.get_iterator()
    while not iterator.is_done():
        print(iterator.current())
        iterator.next()

    # 2. A FilterIterator that filters results from another FilterIterator
    print("FilterIterator that filters results from another FilterIterator:")
    filter_iterator = FilterIterator(my_array.get_iterator(), lambda x: isinstance(x, int))
    filter_iterator2 = FilterIterator(filter_iterator, lambda x: x % 2 == 0)
    while not filter_iterator2.is_done():
        print(filter_iterator2.current())
        filter_iterator2.next()

    # 3. A FilterIterator that filters out everything
    print("FilterIterator that filters out everything:")
    filter_iterator3 = FilterIterator(my_array.get_iterator(), lambda x: False)
    while not filter_iterator3.is_done():
        print(filter_iterator3.current())
        filter_iterator3.next()

    # 4. A ReverseIterator
    print("ReverseIterator:")
    reverse_iterator = ReverseIterator(my_array.get_iterator())
    while not reverse_iterator.is_done():
        print(reverse_iterator.current())
        reverse_iterator.next()

    # 5. A ReverseIterator that takes a FilterIterator, and thus outputs the results of the Filter in reverse order
    print("ReverseIterator that takes a FilterIterator:")
    filter_iterator4 = FilterIterator(my_array.get_iterator(), lambda x: isinstance(x, int))
    reverse_iterator2 = ReverseIterator(filter_iterator4)
    while not reverse_iterator2.is_done():
        print(reverse_iterator2.current())
        reverse_iterator2.next()

if __name__ == '__main__':
    main()