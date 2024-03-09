from databases import Database
from commands import AddCommand, UpdateCommand, RemoveCommand, MacroCommand
from queue import Queue
class Invoker:
    """
    Invoker to execute and undo commands
    """
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command:
            self.command.execute()

    def undo_command(self):
        if self.command:
            self.command.undo()
class Processor:
    """
    Processor to read commands from a file, execute them,
    and display the databases, simulates a client application
    """
    def __init__(self, command_file):
        self.command_file = command_file
        self.databases = {}
        self.command_queue = Queue()
        self.macro_stack = []
        self.executed_commands = []

    def create_command(self, command_type, db, key, value=None):
        if command_type == 'A':
            return AddCommand(db, key, value)
        elif command_type == 'U':
            return UpdateCommand(db, key, value)
        elif command_type == 'R':
            return RemoveCommand(db, key)
        else:
            raise ValueError(f"Unknown command type: {command_type}")

    def read_commands(self):
        with open(self.command_file, 'r') as file:
            for line in file:
                parts = line.strip().split(' ')
                command_type = parts[0]

                if command_type in ('B', 'E'):
                    self.handle_macro_commands(command_type)
                else:
                    db_id = parts[1]
                    key = parts[2]
                    value = ' '.join(parts[3:]) if command_type in ('A', 'U') else None
                    db = self.databases.get(db_id)
                    if db is None and command_type != 'U':
                        db = self.databases[db_id] = Database(db_id)
                    if db is not None:
                        command = self.create_command(command_type, db, key, value)
                        if self.macro_stack:
                            self.macro_stack[-1].add(command)
                        else:
                            self.command_queue.put(command)

    def handle_macro_commands(self, command_type):
        if command_type == 'B':
            self.macro_stack.append(MacroCommand())
        elif command_type == 'E':
            if self.macro_stack:
                macro = self.macro_stack.pop()
                if self.macro_stack:
                    self.macro_stack[-1].add(macro)
                else:
                    self.command_queue.put(macro)

    def execute(self):
        invoker = Invoker()
        while not self.command_queue.empty():
            command = self.command_queue.get()
            invoker.set_command(command)
            invoker.execute_command()
            self.executed_commands.append(command)

    def undo(self):
        invoker = Invoker()
        for command in reversed(self.executed_commands):
            invoker.set_command(command)
            invoker.undo_command()
            print()

    def display_databases(self):
        print("Contents of Databases:")
        for db in self.databases.values():
            db.display(show_db_id=True)
            print()