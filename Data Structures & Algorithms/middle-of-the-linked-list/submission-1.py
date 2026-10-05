# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        if(head):
            j = head.next

        while(j is not None):
            i = i.next
            j = j.next
            if(j is not None):
                j = j.next
        
        return i