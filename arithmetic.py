def fibonacci(number):
    if number < 0:
        return 'there is no negative number in the fibonacci sequence'
    a, b = 0, 1
    while a <= number:
        print(a)
        a, b = b, a + b


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return 'could not find solution'


def isPalindrome(number):
    if number < 0: return False
    reverseNum = 0
    testNum = number
    while testNum > 0:
        reverseNum = reverseNum * 10 + testNum % 10
        testNum = testNum // 10
    return reverseNum == number


def romanToInt(romanNum):
    romanNumbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in range(len(romanNum) - 1):
        if romanNumbers[romanNum[i]] < romanNumbers[romanNum[i + 1]]:
            integer -= romanNumbers[romanNum[i]]
        else:
            integer += romanNumbers[romanNum[i]]
    integer += romanNumbers[romanNum[-1]]
    return integer

# print(romanToInt('LVIII'))

def longestCommonPrefix(strs):
    if not strs:
        return ''

    prefix = ''
    min_length = min([len(s) for s in strs])

    for i in range(min_length):
        current_char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != current_char:
                return prefix

        prefix += current_char

    return prefix

# print(longestCommonPrefix(['jaonh', 'james', 'january']))

def isValid(s):
    parentheses = {'(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{'}
    i = 0
    while i < len(s):
        if parentheses[s[i]] == parentheses[s[-1-i]]:
            i += 1
            continue
        else:
            return False

    return True

print(isValid("()[]{}"))

str = "abcddcba"
i = 2
print(str[i], str[-1 - i])

def isValid(s):
    parentheses = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in s:
        if char in parentheses:
            stack.append(char)
        elif not stack or parentheses[stack.pop()] != char:
            return False

    return not stack
