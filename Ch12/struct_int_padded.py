import struct

bits = struct.pack('>i3xi', -4, -2)
print(bits)  # prints '\xff\xff\xff\xfc\x00\x00\x00\xff\xff\xff\xfe'

first, second = struct.unpack('>i3xi', bits)
print(first, second)  # prints '-4 -2'

wrong = struct.unpack('<i3xi', bits)    # wrong byte order
print(*wrong)                           # prints '-50331649 -16777217'

wrong = struct.unpack('>f3xf', bits)    # wrong types
print(*wrong)                           # prints 'nan nan'

wrong = struct.unpack('>hh3xhh', bits)  # wrong integer type
print(*wrong)                           # prints '-1 -4 -1 -2'

wrong = struct.unpack('>q3xq', bits)    # data sizes too large
print(*wrong)                           # throws struct.error
