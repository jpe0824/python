class Component:
    def __init__(self):
        pass

    def list(self):
        pass

    def list_all(self):
        pass

    def change_dir(self):
        pass

    def count_files(self):
        pass

    def count_all_files(self):
        pass

    def up(self):
        pass
class File(Component):
    def __init__(self, name):
        self.name = name
        self.parent = None

    def list(self):
        return self.name

    def list_all(self, depth = 0):
        return f"{'   ' * depth}{self.name}\n"

    def count_files(self):
        return 1

    def count_all_files(self):
        return 1
class Directory(Component):
    def __init__(self, name):
        self.name = name
        self.files = []

    def list(self):
        return ', '.join(file.name for file in self.files if isinstance(file, File) or isinstance(file, Directory))

    def list_all(self, depth = 0):
        result = f"{'   ' * depth}{self.name}:\n"
        for file in self.files:
            print(f"Depth: {depth}, File: {file.name}") # Debugging line
            result += file.list_all(depth + 1)
        return result

    def change_dir(self, name):
        for file in self.files:
            if isinstance(file, Directory) and file.name == name:
                return file
        return None

    def count_files(self):
        return sum(1 for file in self.files if isinstance(file, File))

    def count_all_files(self):
        return sum(file.count_all_files() for file in self.files)

    def up(self):
        return self.parent

    def add(self, file):
        self.files.append(file)
        file.parent = self
class DirectoryFactory:
    @staticmethod
    def create_dir_tree(file):
        root = None
        current_dir = None
        stack = []

        for line in file:
            line = line.rstrip()
            depth = len(line) - len(line.lstrip())
            name = line.strip()

            if name.endswith(':'):
                new_dir = Directory(name[:-1])
                if not root:
                    root = new_dir
                while stack and depth <= stack[-1][1]:
                    stack.pop()
                if stack:
                    stack[-1][0].add(new_dir)
                stack.append((new_dir, depth))
                current_dir = new_dir
            else:
                file = File(name)
                while stack and depth <= stack[-1][1]:
                    stack.pop()
                if stack:
                    stack[-1][0].add(file)
                else:
                    current_dir.add(file)

        return root
class Explorer:
    def __init__(self, root):
        self.root = root
        self.current_dir = root

    def process(self):
        while True:
            command = input(f"{self.current_dir.name}> ").strip().split()
            if not command:
                continue

            try:
                if command[0] == 'list':
                    print(self.current_dir.list())
                elif command[0] == 'listall':
                    print(''.join(self.current_dir.list_all()))
                elif command[0] == 'chdir':
                    if len(command) > 1:
                        new_dir = self.current_dir.change_dir(command[1])
                        if new_dir:
                            self.current_dir = new_dir
                        else:
                            print("no such directory")
                elif command[0] == 'up':
                    if self.current_dir.parent:
                        self.current_dir = self.current_dir.parent
                elif command[0] == 'count':
                    print(self.current_dir.count_files())
                elif command[0] == 'countall':
                    print(self.current_dir.count_all_files())
                elif command[0] == 'q':
                    break
                else:
                    print("invalid command")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

def main():
    with open("directory.dat", 'r') as file:
        root = DirectoryFactory.create_dir_tree(file)
    explorer = Explorer(root)
    explorer.process()

if __name__ == "__main__":
    main()