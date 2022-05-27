from hashlib import new
import struct

answer = -360
bits = struct.pack('i', answer)

new_answer, = struct.unpack('i', bits)
print(new_answer)  # prints '-360'
