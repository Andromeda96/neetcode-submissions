# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        l1 = head
        while l1:
            temp = l1.next
            l1.next = prev
            prev = l1
            l1 = temp
        i = 1
        l1 = prev
        tail = prev
        prev = None

        while i<n and l1:
            prev = l1
            l1 = l1.next
            i += 1
        if prev is None:
            tail = l1.next
        else:
            prev.next = l1.next
        prev = None
        l1 = tail
        while l1:
            temp = l1.next
            l1.next = prev
            prev = l1
            l1 = temp

        return prev

