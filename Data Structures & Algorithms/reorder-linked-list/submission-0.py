# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while(curr is not None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        startReverse = head
        totalLen = 0
        traverse = head
        while(traverse is not None):
            totalLen += 1
            traverse = traverse.next
        
        count = 0
        while(count < totalLen//2):
            startReverse = startReverse.next
            count += 1
        startReverseNext = startReverse.next
        startReverse.next = None
        secondaryListHead = self.reverseLL(startReverseNext)
        
        i = head
        j = secondaryListHead

        while(i is not None and j is not None):
            tempI = i.next
            tempJ = j.next
            i.next = j
            j.next = tempI

            i = tempI
            j = tempJ

        







