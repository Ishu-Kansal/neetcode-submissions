class Solution:
    def reverseBits(self, n: int) -> int:
        finalNum = 0x0
        count = 0
        while(count < 32):
            currBit = n & 1
            n = n >> 1
            finalNum = finalNum | currBit
            finalNum = finalNum << 1
            count += 1
        
        return finalNum >> 1