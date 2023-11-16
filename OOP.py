class Book:
    def __init__(self, title, author, price, publisher):
        self.publisher = publisher
        self.price = price
        self.author = author
        self.title = title

    def __set__(self, field, value):
        try:
            self.__dict__[field] = value  # use __dict__ to access the instance attributes
        except (KeyError, ValueError) as e:
            return 'entered key or value is not matching with requirements'

    def __get__(self, field):
        try:
            return self.__dict__[field]  # use __dict__ to access the instance attributes
        except KeyError:
            return 'no attribute with this name'


class Summary(Book):
    def __init__(self, obj: Book, genre):
        super().__init__(obj.title, obj.author, obj.price, obj.publisher)  # call the parent constructor
        self.genre = genre

    def __str__(self):  # define a string representation method for the Summary class
        return f"{self.title} by {self.author} is a {self.genre} book that costs {self.price} and is published by {self.publisher}."  # use f-strings to format the string

    def __len__(self):  # define a length method for the Summary class
        return len(self.title) + len(self.author) + len(self.publisher) + 2  # add 2 for spaces


book = Book('Zero to One', 'Peter Russel', 500, "O'reilly")
summary = Summary(book, 'drama')
print(summary)  # print the summary object
print(summary.__len__())  # print the length of the summary object
