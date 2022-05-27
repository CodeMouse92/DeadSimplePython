import struct
from .book import Book

class Bookshelf:
    fileinfo = struct.Struct('>h')
    version = 1

    def __init__(self, *books):
        self.shelf = [*books]

    def __iter__(self):
        return iter(self.shelf)

    def add_books(self, *books):
        self.shelf.extend(books)

    def write_to_stream(self, stream):
        stream.write(self.fileinfo.pack(self.version))
        for book in self.shelf:
            stream.write(book.serialize())

    @classmethod
    def from_stream(cls, stream):
        size = cls.fileinfo.size
        version, = cls.fileinfo.unpack(stream.read(size))
        if version != 1:
            raise ValueError(f"Cannot open .shlf v{version}; expect v1.")
        size = Book.packer.size
        shelf = Bookshelf()
        while bits := stream.read(size):
            shelf.add_books(Book.deserialize(bits))

        return shelf
