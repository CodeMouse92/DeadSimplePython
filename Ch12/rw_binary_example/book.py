import struct


class Book:

    packer = struct.Struct(">64sx64sx2h")

    def __init__(self, title="", author="", pages=0, pages_read=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.pages_read = pages_read

    def update_progress(self, pages_read):
        self.pages_read = min(pages_read, self.pages)

    def serialize(self):
        return self.packer.pack(
            self.title.encode(),
            self.author.encode(),
            self.pages,
            self.pages_read
        )

    @classmethod
    def deserialize(cls, bits):
        title, author, pages, pages_read = cls.packer.unpack(bits)
        title = title.decode()
        author = author.decode()
        return cls(title, author, pages, pages_read)
