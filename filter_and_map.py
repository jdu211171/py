# The filter function takes two arguments: a function and an iterable. It returns an iterator that contains only the
# elements of the iterable that satisfy the function. For example, if you want to filter out the odd numbers from a list
# of numbers, you can use filter like this:

def is_even(n):
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # [2, 4]


# The map function takes two argument: a function and an iterable. It returns an iterator that contains the results of
# applying the function to each element of the iterable. For example, if you want to square each number in a list of
# numbers, you can use map like this:

def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # [1, 4, 9, 16, 25]


# The difference between filter and map is that filter only keeps the elements that pass a certain condition
# (a boolean value), while map applies any operation (such as arithmetic or string manipulation) to each element and
# returns a new iterable. You can also use lambda functions as arguments for filter and map. A lambda function is an
# anonymous function that can be defined in one line using the syntax lambda arguments: expression
