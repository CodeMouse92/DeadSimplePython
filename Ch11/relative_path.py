from pathlib import Path
path = Path('../some_file.txt')
with open(path, 'r') as file:
    print(file.read())  # this is okay (assuming file exists)

# create empty file if none exists
path.touch()            # okay on Path!
