class MedianFinder:

    def __init__(self):
        self.leftHeap = [] # max heap
        self.rightHeap = [] # min heap
        self.isEven = True

    def balance(self):
        leftLen = len(self.leftHeap)
        rightLen = len(self.rightHeap)
        if(leftLen > rightLen + 1):
            elem = -1*heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap, elem)
        elif(rightLen > leftLen + 1):
            elem = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap, -1*elem)

    def addNum(self, num: int) -> None:
        if(len(self.leftHeap) == 0):
            heapq.heappush(self.leftHeap, -1*num)
        elif(num <= -1*self.leftHeap[0]):
            heapq.heappush(self.leftHeap, -1*num)
            self.balance()
        else:
            heapq.heappush(self.rightHeap, num)
            self.balance()
        self.isEven = not self.isEven
        print(self.leftHeap, self.rightHeap)

    def findMedian(self) -> float:
        if(self.isEven):
            maxLeft = -1*self.leftHeap[0]
            minRight = self.rightHeap[0]
            return (maxLeft + minRight)/2
        elif(len(self.leftHeap) > len(self.rightHeap)):
            return -1*self.leftHeap[0]
        else:
            return self.rightHeap[0]
        return
        