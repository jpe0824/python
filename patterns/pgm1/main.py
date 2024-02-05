from collections import deque

class Queue:
    def __init__(self, storage_impl):
        self.storage = storage_impl

    def add(self, item):
        self.storage.append(item)

    def get(self):
        if not self.storage:
            return None
        return self.storage[0]

    def remove(self):
        if not self.storage:
            raise IndexError("remove from an empty queue")
        return self.storage.popleft()

    def size(self):
        return len(self.storage)

    def clear(self):
        self.storage.clear()

    def changeImpl(self, new_storage_impl):
        new_storage_impl.clear()
        while self.storage:
            new_storage_impl.append(self.storage.popleft())
        self.storage = new_storage_impl

# Test driver code
if __name__ == "__main__":
    # Testing with list
    q = Queue(deque())
    q.add(91)
    q.add(92)
    q.changeImpl(deque([93]))
    q.add(94)
    q.add(95)
    print("Queue with deque:", list(q.storage))  # Convert deque to list for display

    # Testing with another deque (simulating changeImpl)
    q2 = Queue(deque())
    q2.add("91")
    q2.add("92")
    q2.changeImpl(deque(["93"]))
    q2.add("94")
    q2.add("95")
    print("Queue with deque (strings):", list(q2.storage))  # Convert deque to list for display
