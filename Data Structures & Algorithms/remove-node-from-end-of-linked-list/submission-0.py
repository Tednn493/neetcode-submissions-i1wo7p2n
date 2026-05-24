# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        f = head
        s = head
        prev = dummy

        

        for i in range(n):
            f=f.next
        
        if f is None:      
            dummy.next = head.next
            return dummy.next
        
        while f:
            f= f.next
            prev = s
            s = s.next
        
        prev.next = s.next
        return dummy.next

        


        