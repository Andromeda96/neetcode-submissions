# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head
        while l2.next and l2.next.next:
            l1 = l1.next
            l2 = l2.next.next
        second = l1.next
        l1.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        l2 = prev
        l1 = head
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2