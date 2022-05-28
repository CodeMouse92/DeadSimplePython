import re


class Book:
    pattern = re.compile(r'(.+)\((\d+)\)\. (.+)\. (.+)\..*')

    def __set_name__(self, owner, name):
        self.name = name

    def attr(self, attr):
        return f"{self.name}.{attr}"

    def __set__(self, instance, value):
        matches = self.pattern.match(value)
        if not matches:
            raise ValueError("Book data must be specified in APA 7 format.")
        setattr(instance, self.attr('author'), matches.group(1))
        setattr(instance, self.attr('year'), matches.group(2))
        setattr(instance, self.attr('title'), matches.group(3))
        setattr(instance, self.attr('publisher'), matches.group(4))

    def __get__(self, instance, owner=None):
        try:
            title = getattr(instance, self.attr('title'))
            author = getattr(instance, self.attr('author'))
        except AttributeError:
            return "nothing right now"
        return f"{title} by {author}"

    def __delete__(self, instance):
        delattr(instance, self.attr('author'))
        delattr(instance, self.attr('year'))
        delattr(instance, self.attr('title'))
        delattr(instance, self.attr('publisher'))


class BookClub:
    reading = Book()
    reading_next = Book()

    def __init__(self, name):
        self.name = name
        self.members = []

    def new_member(self, member):
        self.members.append(member)
        print(
            "===== - - - - - - - - - =====",
            f"Welcome to the {self.name} Book Club, {member}!",
            f"We are reading {self.reading}",
            "===== - - - - - - - - - =====",
            sep='\n'
        )


mystery_lovers = BookClub("Mystery Lovers")
lattes_and_lit = BookClub("Lattes and Lit")

mystery_lovers.reading = (
    "McDonald, J.C. (2019). "
    "Noah Clue, P.I. AJ Charleson Publishing."
)

lattes_and_lit.reading = (
    "Christie, A. (1926). "
    "The Murder of Roger Ackroyd. William Collins & Sons."
)

print(mystery_lovers.reading)  # prints "'The Murder of Roger Ackroyd..."
print(lattes_and_lit.reading)  # prints "'The Murder of Roger Ackroyd..."


del lattes_and_lit.reading

lattes_and_lit.new_member("Jaime")

lattes_and_lit.reading = (
    "Hillerman, T. (1973). "
    "Dance Hall Of The Dead. Harper and Row."
)

lattes_and_lit.new_member("Danny")

mystery_lovers.reading = (
    "McDonald, J.C. (2019). "
    "Noah Clue, P.I. AJ Charleson Publishing."
)

mystery_lovers.reading_next = (
    "Chesterton, G.K. (1911). The Innocence of Father Brown. "
    "Cassell and Company, Ltd."
)
print(f"Now: {mystery_lovers.reading}")
print(f"Next: {mystery_lovers.reading_next}")


import pprint
pprint.pprint(dir(mystery_lovers))
