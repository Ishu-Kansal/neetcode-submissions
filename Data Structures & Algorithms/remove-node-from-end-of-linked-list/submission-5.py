# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        trav = head
        count = 0
        while(trav is not None):
            trav = trav.next
            count += 1
        
        toGo = count - n
        print(count)

        if(toGo == 0):
            return head.next

        prev = None
        curr = head

        for i in range(toGo):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        return head
        


        
