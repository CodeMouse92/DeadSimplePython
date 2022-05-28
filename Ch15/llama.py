class Quadraped:
    leg_count = 4

    def __init__(self, species):
        self.species = species

class Llama(Quadraped):
    """A quadraped that lives in large rivers."""
    dangerous = True

    def __init__(self):
        self.swimming = False
        super().__init__("llama")

    def warn(self):
        if self.swimming:
            print("Cuidado, llamas!")

    @classmethod
    def feed(cls):
        print("Eats honey with beak.")


llama = Llama()

from pprint import pprint
from xml.dom.minidom import Attr

print("Instance.__dict__:")
pprint(vars(llama))

print("\nLlama class __dict__:")
pprint(vars(Llama))

print("\nQuadruped class __dict__")
pprint(vars(Quadraped))

llama = Llama()

try:
    print(object.__getattribute__(llama, 'swimming'))
except AttributeError as e:
    try:
        __getattr__ = object.__getattribute__(llama, '__getattr__')
    except AttributeError:
        raise e
    else:
        print(__getattr__(llama, 'swimming'))

try:
    print(type.__getattribute__(Llama, 'leg_count'))
except AttributeError as e:
    try:
        __getattr__ = type.__getattribute__(Llama, '__getattr__')
    except AttributeError as e:
        try:
            __getattr__ = type.__getattribute__(Llama, '__getattr__')
        except AttributeError:
            raise e
        print(__getattr__(Llama, 'leg_count'))


# Either of these works!
print(llama.swimming)               # prints 'False'
print(getattr(Llama, 'leg_count'))  # prints '4'

if hasattr(llama, 'larger_than_frogs'):
    print("¡Las llamas son más grandes que las ranas!")

try:
    getattr(llama, 'larger_than_frogs')
except AttributeError:
    pass
else:
    print("¡Las llamas son más grandes que las ranas!")


setattr(llama, 'larger_than_frogs', True)
print(llama.larger_than_frogs)  # prints 'True'
setattr(Llama, 'leg_count', 3)
print(Llama.leg_count)          # prints '3'

Llama.dangerous = False         # this is better
print(llama.dangerous)          # prints 'False', looks OK?
print(Llama.dangerous)          # prints 'False', we are safe now

print(llama.larger_than_frogs)  # prints 'True'
# del llama.larger_than_frogs
delattr(llama, 'larger_than_frogs')
print(llama.larger_than_frogs)  # raises AttributeError
