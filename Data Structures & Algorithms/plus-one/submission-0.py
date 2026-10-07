class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        newL = []
        i = 0
        while(carry == 1 or i < len(digits)):
            currSum = carry
            if(i < len(digits)):
                currSum += digits[i]
            newL.append((currSum) % 10)
            carry = currSum // 10
            i += 1

        newL.reverse()

        return newL