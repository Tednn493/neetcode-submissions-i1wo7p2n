# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head

        if not s:
            return False

        f = head.next
        while f and f.next and s:
            if f==s:
                return True
            else:
                f=f.next.next
                s=s.next
        
        return False
        