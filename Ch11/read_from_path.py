from pathlib import PosixPath

# path = PosixPath('/home/jason/.bash_history')
# path = PosixPath.joinpath(PosixPath.home(), '.bash_history')
# path = PosixPath.home() / '.bash_history'
path = PosixPath('~/.bash_history').expanduser()

with path.open('r') as file:
    for line in file:
        continue
    print(line.strip())
