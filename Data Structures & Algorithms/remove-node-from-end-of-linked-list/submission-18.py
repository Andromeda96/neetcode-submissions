# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        prev = None
        i = 0
        while i < n:
            fast = fast.next
            i += 1
        if not fast:
            head = head.next
        else:
            while fast:
                prev = slow
                slow = slow.next
                fast = fast.next

            prev.next = slow.next
        return head

