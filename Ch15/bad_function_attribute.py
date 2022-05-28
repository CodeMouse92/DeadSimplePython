def skit():
    print(skit.actor)


skit.actor = "John Cleese"
skit()    # prints "John Cleese"

sketch = skit
sketch()  # prints "John Cleese"
sketch.actor = "Eric Idle"
sketch()  # prints "Eric Idle"

skit()    # prints "Eric Idle"...yikes!
