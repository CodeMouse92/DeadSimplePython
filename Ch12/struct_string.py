import struct

bits = struct.pack('>4s', b"Hi!")
print(bits)  # prints 'Hi!\x00'

bits = struct.pack('>4p', b"Hi!")
print(bits)  # prints '\x03Hi!'
