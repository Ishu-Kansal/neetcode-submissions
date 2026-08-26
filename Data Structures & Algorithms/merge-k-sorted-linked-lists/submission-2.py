# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedList = []

        for i in range(len(lists)):
            node = lists[i]
            if(node is not None):
                # orders (value, index) tuple
                heapq.heappush(sortedList, (node.val, i))

        head = ListNode()
        curr = head
        while(len(sortedList) > 0):
            _, currSmallestIdx = heapq.heappop(sortedList)
            
            toChange = lists[currSmallestIdx]
            curr.next = toChange
            newNode = toChange.next
            lists[currSmallestIdx] = newNode
            if(newNode is not None):
                heapq.heappush(sortedList, (newNode.val, currSmallestIdx))
            toChange.next = None
            curr = curr.next
        
        return head.next

