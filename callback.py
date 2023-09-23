def my_callback_function(arg1, arg2):
    result = arg1 + arg2
    print(f'The result is {result}')


def perform_operation(x, y, z, callback):
    result = x + y
    callback(result, z)


perform_operation(5, 3, 8, my_callback_function)
