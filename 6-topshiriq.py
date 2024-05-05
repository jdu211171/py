import os


def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6


def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
    return sum(nums)


def rotate_left3(nums):
    return nums[1:] + nums[:1]


def reverse3(nums):
    return nums[::-1]


def max_end3(nums):
    return [max(nums[0], nums[-1])] * 3


def sum2(nums):
    return sum(nums[:2])


def middle_way(a, b):
    return [a[1], b[1]]


def make_ends(nums):
    return [nums[0], nums[-1]]


def has23(nums):
    return 2 in nums or 3 in nums


def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]


def make_pi():
    return [3, 1, 4]


def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and isinstance(board[condition[0]], str):
            return True
    return False


def print_board(board):
    if 'TERM' in os.environ:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    for i in range(0, 9, 3):
        for j in range(3):
            if board[i + j] == 'X':
                print('\033[31m' + 'X' + '\033[0m', end=' ')
            elif board[i + j] == 'O':
                print('\033[34m' + 'O' + '\033[0m', end=' ')
            else:
                print(board[i + j], end=' ')
            if j < 2:
                print('|', end=' ')
        print()
        if i < 6:
            print('---------')


def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    current_player = 'X'

    while True:
        print_board(board)
        if not any(item.isdigit() for item in board):
            if not check_win(board):
                print("O'yin durrang bilan tugadi.")
                break
        move = input(f"Janob {current_player}, o'zingizning yurishingizni belgilang (1-9): ")
        if board[int(move) - 1] != 'X' and board[int(move) - 1] != 'O':
            board[int(move) - 1] = current_player
            if check_win(board):
                print_board(board)
                print(f"Janob {current_player} g'alaba qozondi!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Iltimos doskadagi yurishlardan birini yuring.")


if __name__ == "__main__":
    tic_tac_toe()
