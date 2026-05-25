# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        for i in range(1,len(lists)):
            lists[i] = self.mergedList(lists[i-1],lists[i])
        return lists[-1]

    def mergedList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                temp = l1.next
                tail.next = l1
                l1 = temp
            else:
                temp = l2.next
                tail.next = l2
                l2 = temp
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next




        