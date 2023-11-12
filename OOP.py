class Book:
    def __init__(self, title, author, price, publisher):
        self.publisher = publisher
        self.price = price
        self.author = author
        self.title = title

    def __set__(self, field, value):
        if isinstance(value, str) and value:
            self.__dict__[field] = value  # use __dict__ to access the instance attributes

    def __get__(self, field):
        try:
            return self.__dict__[field]  # use __dict__ to access the instance attributes
        except KeyError:
            return None  # return None if the attribute does not exist


class Summary(Book):
    def __init__(self, book):
        super().__init__(book.title, book.author, book.price, book.publisher)  # call the parent constructor

    def __str__(self):  # define a string representation method for the Summary class
        return f"{self.title} by {self.author} is a book that costs {self.price} and is published by {self.publisher}."  # use f-strings to format the string

    def __len__(self):  # define a length method for the Summary class
        return len(self.title) + len(self.author) + len(self.publisher) + 2  # add 2 for spaces


book = Book('Zero to One', 'Peter Russel', 500, "O'reilly")
summary = Summary(book)
print(summary)  # print the summary object
print(summary.__len__())  # print the length of the summary object
