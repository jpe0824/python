from commands import AddCommand, UpdateCommand, RemoveCommand, BeginTransactionCommand, EndTransactionCommand
from databases import Database

class CommandProcessor:
    def __init__(self, command_file):
        self.command_file = command_file
        self.commands = []
        self.databases = {}

    def read_commands(self):
        with open(self.command_file, 'r') as file:
            for line in file:
                parts = line.strip().split()
                command_type = parts[0]
                if command_type == 'A':
                    self.commands.append(AddCommand(parts[2], parts[3]))
                elif command_type == 'U':
                    self.commands.append(UpdateCommand(parts[2], parts[3]))
                elif command_type == 'R':
                    self.commands.append(RemoveCommand(parts[2]))
                elif command_type == 'B':
                    self.commands.append(BeginTransactionCommand())
                elif command_type == 'E':
                    self.commands.append(EndTransactionCommand())

    def execute_commands(self):
        for command in self.commands:
            if isinstance(command, BeginTransactionCommand):
                print("Beginning a Macro")
            elif isinstance(command, EndTransactionCommand):
                print("Ending a Macro")
            else:
                database_id = command.database_id if hasattr(command, 'database_id') else 'default'
                if database_id not in self.databases:
                    self.databases[database_id] = Database(database_id)
                command.execute(self.databases[database_id])

    def undo_commands(self):
        for command in reversed(self.commands):
            if isinstance(command, BeginTransactionCommand):
                print("Begin Undoing Macro")
            elif isinstance(command, EndTransactionCommand):
                print("End Undoing Macro")
            else:
                database_id = command.database_id if hasattr(command, 'database_id') else 'default'
                command.undo(self.databases[database_id])

    def display_databases(self):
        for database in self.databases.values():
            database.display()
