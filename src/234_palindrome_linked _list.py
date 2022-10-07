# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            print("list is empty!")
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        l, r = 0, len(nums)-1
        while l<r:
            if nums[l]!=nums[r]:
                return False
            l += 1
            r -= 1
        return True

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    

def is_palindromic_linked_list(head):
    if not head or not head.next:
        return True
    
    # find middle of linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow)
    copy_head_second_half = head_second_half

    # compare the first and second half
    while head and head_second_half:
        if head.value != head_second_half.value:
            break

        head = head.next
        head_second_half = head_second_half.next
    
    reverse(copy_head_second_half)

    if not head or not head_second_half:
        return True
    
    return False

def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev