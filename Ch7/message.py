class Message:

    def __init__(self):
        self.__format = "UTF-8"


msg = Message()
# print(msg.__format)  # AttributeError
print(msg._Message__format)
