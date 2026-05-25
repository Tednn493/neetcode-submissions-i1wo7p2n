# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0

        while l1 and l2:
            total = l1.val+l2.val + carry
            carry = 0
            if total > 9:
                tail.next = ListNode(total%10,None)
                carry= 1
            else:
                tail.next = ListNode(total,None)
            l1 = l1.next
            l2 = l2. next
            tail = tail.next
        
        if l1:
            while l1:
                total = l1.val + carry
                carry = 0
                if total > 9:
                    tail.next = ListNode(total%10,None)
                    carry= 1
                else:
                    tail.next = ListNode(total,None)
                l1 = l1.next
                tail = tail.next
        else:
            while l2:
                total = l2.val + carry
                carry = 0
                if total > 9:
                    tail.next = ListNode(total%10,None)
                    carry= 1
                else:
                    tail.next = ListNode(total,None)
                l2 = l2.next
                tail = tail.next
        
        if carry:
            tail.next = ListNode(carry,None)

        return dummy.next
            
        