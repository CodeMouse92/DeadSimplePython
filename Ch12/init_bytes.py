bits = bytes(0b110)
print(bits)  # prints '0x00\x00\x00\x00\x00\0x00'

# bits = bytes((0b110,))
bits = bytearray(b'\x06')
print(bits)  # prints "b'\x06'"

bits = bytes('☺', encoding='utf-8')
print(bits)  # print "b'\xe2\x98\xba'"
