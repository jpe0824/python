class Visitor:
    def visit_file(self, file):
        pass

    def visit_directory(self, directory):
        pass

class ListVisitor(Visitor):
    def visit_file(self, file):
        print(file.name)

    def visit_directory(self, directory):
        print(directory.name)
        directory.acceptChildren(self)

class ListAllVisitor(Visitor):
    def __init__(self):
        self.depth = 0

    def visit_file(self, file):
        print(' ' * self.depth + file.name)

    def visit_directory(self, directory):
        print(' ' * self.depth + directory.name)
        self.depth += 1
        directory.acceptChildren(self)
        self.depth -= 1

class FindVisitor(Visitor):
    def __init__(self, name):
        self.name = name

    def visit_file(self, file):
        if file.name == self.name:
            print(f"Found leaf: {file.name}")

    def visit_directory(self, directory):
        if directory.name == self.name:
            print(f"Found directory: {directory.name}")
            directory.acceptChildren(ListAllVisitor())

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
    # Setup a simple directory structure
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

    print("Listing all:")
    listAllVisitor = ListAllVisitor()
    root.acceptChildren(listAllVisitor)

    print("\nFinding 'file2':")
    findVisitor = FindVisitor("file2")
    root.acceptChildren(findVisitor)

if __name__ == "__main__":
    main()