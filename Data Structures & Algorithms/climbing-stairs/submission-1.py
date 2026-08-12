class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2

        if(n == 1):
            return 1
        if(n == 2):
            return 2

        for i in range(n-2):
            newOne = first + second
            first = second
            second = newOne
        
        return second