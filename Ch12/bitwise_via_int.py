def bitwise_and(left, right, *, byteorder):
    size = max(len(left), len(right))
    left = int.from_bytes(left, byteorder=byteorder)
    right = int.from_bytes(right, byteorder=byteorder)
    result = left & right
    return result.to_bytes(size, byteorder, signed=True)


bits = b'\xcc\xcc\xcc'   # 0b110011001100110011001100
bitfilter = b'\xaa\xaa'  # 0b1010101010101010

result = bitwise_and(bits, bitfilter, byteorder='big')
print(result)            # prints "b'\x00\x88\x88'"
