class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []

        def processBit(num)-> int:
            count = 0
            while(num):
                num = num & (num-1)
                count += 1
            return count

        for i in range(n+1):
            arr.append(processBit(i))
        
        return arr