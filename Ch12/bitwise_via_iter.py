# Thanks to Daniel Foerster for helping create this solution.
import itertools


def bitwise_and(left, right, *, byteorder):
    pad_left = itertools.repeat(0, max(len(right) - len(left), 0))
    pad_right = itertools.repeat(0, max(len(left) - len(right), 0))

    if byteorder == 'big':
        left_iter = itertools.chain(pad_left, left)
        right_iter = itertools.chain(pad_right, right)
    elif byteorder == 'little':
        left_iter = itertools.chain(left, pad_left)
        right_iter = itertools.chain(right, pad_right)
    else:
        raise ValueError("byteorder must be either 'little' or 'big'")

    return bytes(l & r for l, r in zip(left_iter, right_iter))


bits = b'\xcc\xcc\xcc'   # 0b110011001100110011001100
bitfilter = b'\xaa\xaa'  # 0b1010101010101010

result = bitwise_and(bits, bitfilter, byteorder='big')
print(result)            # prints "b'\x00\x88\x88'"
