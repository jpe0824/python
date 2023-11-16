import os
import sys
import sqlite3
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python readfiles.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    conn = sqlite3.connect('files.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS files (
            ext TEXT,
            path TEXT,
            fname TEXT
        )
    ''')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if '.' in file and not file.startswith(('.', '_')):
                ext = file.split('.')[-1]
                path = Path(root).resolve()
                c.execute("INSERT INTO files VALUES (?, ?, ?)", (ext, str(path), file))

    conn.commit()

    rows = c.execute("SELECT * FROM files").fetchall()
    with open('files-part1.txt', 'w') as f:
        for row in rows:
            f.write(str(row) + '\n')

    conn.close()

if __name__ == "__main__":
    main()