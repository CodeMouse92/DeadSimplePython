import struct

bits = struct.pack('>2i?', 4, 2, True)
print(bits)  # prints '\x00\x00\x00\x04\x00\x00\x00\x02\x01'
