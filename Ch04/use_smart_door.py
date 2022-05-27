# import smart_door
# smart_door.open()
# smart_door.close()

# from smart_door import open, close
from smart_door import open as door_open
from smart_door import close
door_open()
close()

somefile = open("data.txt", "r")
# ...work with the file...
somefile.close()
