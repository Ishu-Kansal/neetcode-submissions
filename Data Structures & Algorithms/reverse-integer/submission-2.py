class Solution:
    def reverse(self, x: int) -> int:
        MAXNUM = 2 ** 31 // 10
        MAXREM = 2 ** 31 % 10

        curr = 0
        isNeg = (x < 0)
        if(isNeg):
            x = x * -1

        while(x > 0):
            lastDigit = x % 10
            if(curr > MAXNUM):
                return 0
            if(curr == MAXNUM and lastDigit > MAXREM):
                return 0
                
            curr *= 10
            curr += lastDigit
            x = x // 10
        
        if(isNeg):
            return curr * -1
        return curr