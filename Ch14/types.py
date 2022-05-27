print(type("Hello"))    # prints "<class 'str'>"
print(type(123))        # prints "<class 'int'>"

class Thing: pass
print(type(Thing))      # prints "<class 'type'>"

something = Thing()
print(type(something))  # prints "<class '__main__.Thing'>"

print(type(type))       # prints "<class 'type'>"
