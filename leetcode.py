# Valid Parentheses

def isValid(s):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs.keys():
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
        else:
            # If the character is not an opening or closing bracket, it's invalid
            return False
    # If the stack is empty at the end, all brackets are matched and valid
    return not stack


print(isValid('({[]})'))


# Merge Two Sorted Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()  # Dummy node to serve as the head of the merged list
    tail = dummy  # Tail pointer to keep track of the last node in the merged list

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Append any remaining nodes from list1 or list2
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next  # Head of the merged list

# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)
#
# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)
#
# merged_list = mergeTwoLists(list1, list2)
#
# while merged_list:
#     print(merged_list.val, end=" -> ")
#     merged_list = merged_list.next

# def removeDuplicates(nums):
#     for i in range(len(nums)):
        # if nums[i] == nums[]