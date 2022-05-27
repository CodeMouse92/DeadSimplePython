def verify(bits):
    with memoryview(bits) as view:
        for i in range(3, len(view), 5):
            if view[i:i+2] != b'\xff\xff':
                return False
    return True


good = b'\x11\x22\x33\xff\xff\x44\x55\x66\xff\xff\x77\x88'
print(verify(good))  # prints 'True'

nope = b'\x11\x22\x33\xff\x44\x55\x66\x77\xff\x88\x99\xAA'
print(verify(nope))  # prints 'False'
