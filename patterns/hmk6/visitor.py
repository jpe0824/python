class Visitor:
    def visit_file(self, file):
        pass

    def visit_directory(self, directory):
        pass
class ListVisitor(Visitor):
    def __init__(self):
        self.depth = 0

    def visit_file(self, file):
        print(' ' * self.depth + file.name)

    def visit_directory(self, directory):
        print(' ' * self.depth + directory.name)
        self.depth += 1
        directory.acceptChildren(self)
        self.depth -= 1
class CountVisitor(Visitor):
    def __init__(self):
        self.count = 0

    def visit_file(self, file):
        self.count += 1

    def visit_directory(self, directory):
        directory.acceptChildren(self)
class CountAllVisitor(Visitor):
    def __init__(self):
        self.count = 0

    def visit_file(self, file):
        self.count += 1

    def visit_directory(self, directory):
        self.count += 1
        directory.acceptChildren(self)
class FindVisitor(Visitor):
    def __init__(self, name):
        self.name = name

    def visit_file(self, file):
        if file.name == self.name:
            print(f"Found leaf: {file.name}")

    def visit_directory(self, directory):
        if directory.name == self.name:
            print(f"Found directory: {directory.name}")
            directory.acceptChildren(ListVisitor())
        else:
            directory.acceptChildren(self)
class CountLeavesVisitor(Visitor):
    def __init__(self):
        self.count = 0

    def visit_file(self, file):
        self.count += 1

    def visit_directory(self, directory):
        directory.acceptChildren(self)
class EverythingVisitor(Visitor):
    def __init__(self):
        self.count = 0

    def visit_file(self, file):
        self.count += 1

    def visit_directory(self, directory):
        self.count += 1
        directory.acceptChildren(self)
class ListRootsVisitor(Visitor):
    def __init__(self):
        self.depth = 0

    def visit_file(self, file):
        if self.depth == 0:
            print(file.name)

    def visit_directory(self, directory):
        if self.depth == 0:
            print(directory.name)
        self.depth += 1
        directory.acceptChildren(self)
        self.depth -= 1
class Component:
    def accept(self, visitor):
        pass
class File(Component):
    def __init__(self, name):
        self.name = name
        self.parent = None

    def accept(self, visitor):
        visitor.visit_file(self)
class Directory(Component):
    def __init__(self, name):
        self.name = name
        self.files = []
        self.parent = None

    def accept(self, visitor):
        visitor.visit_directory(self)

    def acceptChildren(self, visitor):
        for file in self.files:
            file.accept(visitor)

    def add(self, file):
        self.files.append(file)
        file.parent = self

def main():
    root = Directory("root")
    dir1 = Directory("dir1")
    file1 = File("file1")
    file2 = File("file2")
    dir2 = Directory("dir2")
    file3 = File("file3")

    root.add(dir1)
    dir1.add(file1)
    dir1.add(file2)
    root.add(dir2)
    dir2.add(file3)

    print("Listing:")
    root.acceptChildren(ListVisitor())

    print("\nCounting leaves:")
    countLeavesVisitor = CountLeavesVisitor()
    root.acceptChildren(countLeavesVisitor)
    print(f"Number of leaves: {countLeavesVisitor.count}")

    print("\nCounting all:")
    countAllVisitor = CountAllVisitor()
    root.acceptChildren(countAllVisitor)
    print(f"Total number of nodes: {countAllVisitor.count}")

    print("\nEverything:")
    everythingVisitor = EverythingVisitor()
    root.acceptChildren(everythingVisitor)
    print(f"Total number of nodes: {everythingVisitor.count}")

    print("\nFinding 'file2':")
    findVisitor = FindVisitor("file2")
    root.acceptChildren(findVisitor)

    print("\nListing roots:")
    root.acceptChildren(ListRootsVisitor())

if __name__ == "__main__":
    main()
