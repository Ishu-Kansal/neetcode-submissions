class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        
        newNum = 0
        temp = x
        power = 1
        while(temp > 0):
            newNum *= 10
            newNum += temp % 10
            temp //= 10
        
        print(newNum)
        return (newNum == x)