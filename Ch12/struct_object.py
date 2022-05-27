import struct

packer = struct.Struct('iif')


def number_grinder(n):
    for right in range(1, 100):
        left = right % n
        result = left / right
        yield packer.pack(left, right, result)


for bits in number_grinder(5):
    print(*packer.unpack(bits))
