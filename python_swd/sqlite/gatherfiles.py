import os
import sys
import sqlite3
import zipfile

def main():
    if len(sys.argv) < 3:
        print("Usage: python gatherfiles.py <database> <extensions>")
        sys.exit(1)

    database = sys.argv[1]
    extensions = sys.argv[2:]

    conn = sqlite3.connect(database)
    c = conn.cursor()

    for ext in extensions:
        c.execute("SELECT * FROM files WHERE ext LIKE ?", (ext,))
        rows = c.fetchall()

        with zipfile.ZipFile(f'{ext}.zip', 'w') as zipf:
            for row in rows:
                path, fname = row[1], row[2]
                full_path = os.path.join(path, fname)
                if os.path.exists(full_path):
                    zipf.write(full_path, arcname=os.path.join(path.replace(':', ''), fname))

        print(f'{len(rows)} {ext} files gathered')

    conn.close()

if __name__ == "__main__":
    main()