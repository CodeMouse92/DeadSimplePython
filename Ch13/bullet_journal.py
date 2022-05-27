from calendar import month


class Collection:

    def __init__(self, title, page_start, length=1):
        self.title = title
        self.page_start = page_start
        self.page_end = page_start + length - 1
        self.item = []

    def __str__(self):
        return self.title

    def expand(self, by):
        self.page_end += by

    def add_item(self, bullet, note, signifier=None):
        """Adds an item to the monthly log."""


class MonthlyLog(Collection):

    def __init__(self, month, year, page_start, length=2):
        super().__init__(f"{month} {year}", page_start, length)
        self.events = []

    def __str__(self):
        return f"{self.title} (Monthly Log)"

    def add_event(self, event, date=None):
        """Logs an event for the given date (today by default)."""


class FutureLog(Collection):

    def __init__(self, start_month, page_start):
        super().__init__("Future Log", page_start, 4)
        self.start = start_month
        self.months = [start_month]  # TODO: Add other five months.

    def add_item(self, bullet, note, signifier=None, month=None):
        """Adds an item to the future log for the given month."""


log = FutureLog('May 2023', 5)
log.add_item('June 2023', '.', 'Clean mechanical keyboard')
print(log)  # prints "Future Log"

monthly = MonthlyLog('April', '2023', 9)
monthly.add_event('Finally learned Python inheritance!')
monthly.add_item('.', 'Email Ben re: coffee meeting')
print(monthly)  # prints "April 2023 (Monthly Log)"

to_read = Collection("Books to Read", 17)
to_read.add_item('.', 'Anne of Avonlea')
print(to_read)  # prints "Books to Read"
