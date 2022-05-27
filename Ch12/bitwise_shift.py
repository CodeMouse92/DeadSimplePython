print(bin(0b1100 << 4))   # prints '0b11000000

print(bin(0b1100 >> 4))   # prints  '0b0' (0b0...0000)
print(bin(-0b1100 >> 4))  # prints '-0b1' (0b1...1111)
