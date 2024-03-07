from processor import CommandProcessor

def main(command_file):
    processor = CommandProcessor(command_file)
    processor.read_commands()
    processor.execute_commands()
    print("Contents of Databases:")
    processor.display_databases()
    print("Undoing Commands:")
    processor.undo_commands()
    print("After Undoing:")
    processor.display_databases()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <command_file>")
        sys.exit(1)
    main(sys.argv[1])
