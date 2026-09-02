class Solution:
    def climbStairs(self, n: int) -> int:
        short = 1
        long = 2

        if(n == 1 or n == 2):
            return n
        for i in range(2, n):
            temp = long
            long = short + long
            short = temp

        return long