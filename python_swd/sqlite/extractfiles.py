import os
import sys
import re
import zipfile

def main():
    if len(sys.argv) != 3:
        print("Usage: python extractfiles.py <zipfile> <regex>")
        sys.exit(1)

    zip_file = sys.argv[1]
    regex = re.compile(sys.argv[2])

    with zipfile.ZipFile(zip_file, 'r') as zipf:
        files = [f for f in zipf.namelist() if regex.match(os.path.basename(f))]
        for file in files:
            zipf.extract(file)

    print(f'{len(files)} files extracted')

if __name__ == "__main__":
    main()