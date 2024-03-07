from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, database):
        pass

    @abstractmethod
    def undo(self, database):
        pass

class AddCommand(Command):
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def execute(self, database):
        database.add(self.key, self.value)

    def undo(self, database):
        database.remove(self.key)

class UpdateCommand(Command):
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.old_value = None

    def execute(self, database):
        self.old_value = database.get(self.key)
        database.update(self.key, self.value)

    def undo(self, database):
        database.update(self.key, self.old_value)

class RemoveCommand(Command):
    def __init__(self, key) -> None:
        self.key = key
        self.value = None

    def execute(self, database):
        self.value = database.get(self.key)
        database.remove(self.key)

    def undo(self, database):
        database.add(self.key, self.value)

class BeginTransactionCommand(Command):
    def execute(self, database):
        pass # No action needed

    def undo(self, database):
        pass # No action needed

class EndTransactionCommand(Command):
    def execute(self, database):
        pass # No action needed

    def undo(self, database):
        pass # No action needed