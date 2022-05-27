from abc import ABC, abstractmethod
from collections.abc import Sequence


class Palindromable(ABC):

    @abstractmethod
    def __reversed__(self): pass

    @abstractmethod
    def __iter__(self): pass

    @abstractmethod
    def __str__(self): pass


class LetterPalindrome(Palindromable):

    def __init__(self, string):
        self._raw = string
        self._stripped = ''.join(filter(str.isalpha, string.lower()))

    def __str__(self):
        return self._raw

    def __iter__(self):
        return self._stripped.__iter__()

    def __reversed__(self):
        return reversed(self._stripped)

    @classmethod
    def __subclasshook__(cls, C):
        if issubclass(C, Sequence):
            return True
        return NotImplemented


def check_palindrome(sequence):

    if not isinstance(sequence, Palindromable):
        raise TypeError("Cannot check for palindrome on that type.")

    for c, r in zip(sequence, reversed(sequence)):
        if c != r:
            print(f"NON-PALINDROME: {sequence}")
            return False
    print(f"PALINDROME: {sequence}")
    return True


canal = LetterPalindrome("A man, a plan, a canal - Panama!")
print(check_palindrome(canal))                         # prints 'True'

bolton = LetterPalindrome("Bolton")
print(check_palindrome(bolton))                        # prints 'False'

print(check_palindrome([1, 2, 3, 2, 1]))               # prints 'True'
print(check_palindrome((1, 2, 3, 2, 1)))               # prints 'True'

print(check_palindrome('racecar'))                     # prints 'True'
print(check_palindrome('race car'))                    # prints 'False'
print(check_palindrome(LetterPalindrome('race car')))  # prints 'True'

print(check_palindrome({1, 2, 3, 2, 1}))               # raises TypeError
