class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        stack = []
        nums.sort()
        totals = []

        numSet = set()
        for num in nums:
            numSet.add(num)
            stack.append([num])
        
        while(len(stack) > 0):
            print(stack)
            currList = stack[-1]
            stack.pop()
            currSum = sum(currList)
            if(currSum == target):
                totals.append(currList)
                continue

            biggestElem = currList[-1]

            for num in nums:
                if(num >= biggestElem and num + currSum <= target):
                    newList = currList.copy()
                    newList.append(num)
                    stack.append(newList)

        return totals


