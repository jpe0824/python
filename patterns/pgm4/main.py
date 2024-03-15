from processor import Processor

def main(command_file):
    processor = Processor(command_file)
    processor.read_commands()
    processor.execute()
    processor.display_databases()
    processor.undo()
    processor.display_databases()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <command_file>")
        sys.exit(1)
    main(sys.argv[1])