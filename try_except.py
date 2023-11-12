# try:
#     print('try part started')
#     print(5/0)
#     print('try part ended')
# except ZeroDivisionError as e:
#     print('except part started')
#     print(e)
#     print('except part ended')
# finally:
#     print('thanks for using our program')

# try:
#     int('a')
#     print(5 / 0)
# except (ZeroDivisionError, ValueError) as e:
#     print(f'error has occurred: ', e)
# finally:
#     print('thanks for using our program')

import error_module as error_module


try:
    error_module
except ZeroDivisionError as e:
    print(f'error has occurred {e}')
finally:
    print('thanks for using our program')
