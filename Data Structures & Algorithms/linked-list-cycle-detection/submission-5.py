# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        ind1 = 0
        ind2 = 0
        while p1 and p2:
            ind2 += 1
            p2 = p2.next
            if p2 == p1:
                return True
            elif p2:
                ind2 += 1
                p2 = p2.next
                if p2 == p1:
                    return True
            else:
                return False
            p1 = p1.next
            ind1 += 1
        
        return False
