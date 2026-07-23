class Solution:
    def getSum(self, a: int, b: int) -> int:
        newNum = 0
        carry = 0
        offset = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            currA = (a >> i) & 1
            currB = (b >> i) & 1
            currBit = ((currA ^ currB) ^ carry)
            carry = int((currA + currB + carry)/2)

            if(currBit):
                newNum = newNum | (currBit << i)
        
        print('carry: ', carry)
        print(f"{newNum:b}")

        if newNum > 0x7FFFFFFF:
            newNum = ~(newNum ^ mask)

        print(f"{newNum:b}")
        return newNum

            