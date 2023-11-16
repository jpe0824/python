import os
import sys
import re
import zipfile

def main():
    # Parse command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python extractfiles.py <zipfile> <regex>")
        sys.exit(1)

    zip_file = sys.argv[1]
    regex = sys.argv[2]

    # Open zip file
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        # For each file, check if basename matches regex and extract if it does
        files = [f for f in zipf.namelist() if re.match(regex, os.path.basename(f))]
        for file in files:
            zipf.extract(file)

    print(f'{len(files)} files extracted')

if __name__ == "__main__":
    main()