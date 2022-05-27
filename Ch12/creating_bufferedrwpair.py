from pathlib import Path
Path('readfrom.dat').write_bytes(b'\xaa\xbb\xcc')

from io import BufferedRWPair
with BufferedRWPair(Path('readfrom.dat').open('rb'), Path('writeto.dat').open('wb')) as buffer:
    data = buffer.read()
    print(data)  # prints "b'\xaa\xbb\xcc'"
    buffer.write(data)

Path('writeto.dat').read_bytes()  # prints "b'\xaa\xbb\xcc'"
