from abc import ABC, abstractmethod
class Command(ABC):
    """
    Abstract class for command pattern
    """
    def __init__(self, db, key, value=None) -> None:
        self.db = db
        self.key = key
        self.value = value

    @abstractmethod
    def execute(self, database):
        pass

    @abstractmethod
    def undo(self, database):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}"
class AddCommand(Command):
    """
    Concrete command class for adding a key-value pair to a database
    """
    def execute(self):
        self.db.add(self.key, self.value)

    def undo(self):
        self.db.remove(self.key)
        print(f"Undid {self.__str__()}")
        self.db.display()
class UpdateCommand(Command):
    """
    Concrete command class for updating a key-value pair in a database
    """
    def execute(self):
        self.old_value = self.db.get(self.key)
        self.db.update(self.key, self.value)

    def undo(self):
        self.db.update(self.key, self.old_value)
        print(f"Undid {self.__str__()}")
        self.db.display()
class RemoveCommand(Command):
    """
    Concrete command class for removing a key-value pair from a database
    """
    def execute(self):
        self.old_value = self.db.get(self.key)
        self.db.remove(self.key)
    def undo(self):
        self.db.add(self.key, self.old_value)
        print(f"Undid {self.__str__()}")
        self.db.display()
class MacroCommand(Command):
    """
    Concrete command class for executing and undoing a sequence of commands
    """
    def __init__(self) -> None:
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def execute(self):
        print("Beginning a macro")
        for command in self.commands:
            command.execute()
        print("Ending a macro\n")

    def undo(self):
        print("Begin Undoing macro\n")
        for command in reversed(self.commands):
            command.undo()
            print(f"\nUndid {command.__str__()}")
            command.db.display()
            print("")
        print("End Undoing macro")