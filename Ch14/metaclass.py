class Gadget(type):

    def __new__(self, name, bases, namespace):
        print(f"Creating a {name} gadget!")
        return super().__new__(self, name, bases, namespace)

    @classmethod
    def __prepare__(cls, name, bases):
        return {'color': 'white'}


class Thingamajig(metaclass=Gadget):
    def __init__(self, widget):
        self.widget = widget

    def frob(self):
        print(f"Frobbing {self.widget}.")


thing = Thingamajig("button")  # also prints "Creating Thingamajig gadget!"
thing.frob()                   # prints "Frobbing button"

print(Thingamajig.color)       # prints "white"
print(thing.__class__)         # prints "<class '__main__.Thingamajig'>"
