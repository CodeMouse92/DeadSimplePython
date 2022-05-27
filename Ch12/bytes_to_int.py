import sys

bits = (-42).to_bytes(4, byteorder=sys.byteorder, signed=True)
answer = int.from_bytes(bits, byteorder=sys.byteorder, signed=True)
print(answer)  # prints '-42'
