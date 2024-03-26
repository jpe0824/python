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

def File(Component):
    def __init__(self, name):
        self.name = name

    def list(self):
        return self.name

    def list_all(self):
        pass

    def count_files(self):
        pass

    def count_all_files(self):
        pass

class Directory(Component):
    def __init__(self, name):
        self.name = name
        self.files = []

    def list(self):
        pass

    def list_all(self):
        pass

    def change_dir(self, name):
        pass

    def count_files(self):
        pass

    def count_all_files(self):
        pass

    def up(self):
        pass

    def add(self, file):
        pass