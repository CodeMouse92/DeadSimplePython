from pathlib import Path
Path('binarybits.dat').write_bytes(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

with open('binarybits.dat', 'br') as file:
    file.seek(-6, 2)
    file.seek(2, 1)
