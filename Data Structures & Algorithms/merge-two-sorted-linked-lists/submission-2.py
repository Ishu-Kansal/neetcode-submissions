# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newHead = ListNode()
        curr = newHead

        while(list1 is not None and list2 is not None):
            firstVal = list1.val
            secondVal = list2.val
            if(secondVal <= firstVal):
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        curr.next = list1 or list2
        
        return newHead.next
        