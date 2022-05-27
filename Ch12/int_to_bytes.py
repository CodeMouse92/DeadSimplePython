import sys

print(sys.byteorder)      # prints 'little'

answer = 42
bits = answer.to_bytes(4, byteorder=sys.byteorder, signed=True)
print(bits.hex(sep=' '))  # prints '2a 00 00 00'

answer = -42
bits = answer.to_bytes(4, byteorder=sys.byteorder, signed=True)
print(bits.hex(sep=' '))  # prints 'd6 ff ff ff'
