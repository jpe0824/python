import os
import sys
import sqlite3
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python readfiles.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    # Connect to SQLite database and create table
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS files (
            ext TEXT,
            path TEXT,
            fname TEXT
        )
    ''')

    # Traverse directory tree and insert file information into database
    for root, dirs, files in os.walk(directory):
        for file in files:
            if '.' in file:
                ext = file.split('.')[-1]
                path = Path(root).resolve()
                c.execute("INSERT INTO files VALUES (?, ?, ?)", (ext, str(path), file))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Query database and write results to text file
    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM files").fetchall()
    with open('files-part1.txt', 'w') as f:
        for row in rows:
            f.write(str(row) + '\n')

    conn.close()

if __name__ == "__main__":
    main()