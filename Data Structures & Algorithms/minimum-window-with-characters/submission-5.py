class Solution:
    def minWindow(self, s: str, t: str) -> str:
        inWindow = {} # stores ONLY letters of significance | letter -> count
        windowHasLetter = False
        tSize = {}

        def checkCompleteness():
            for ch in tSize:
                if(inWindow[ch] < tSize[ch]):
                    return False
            return True    

        for ch in t:
            inWindow[ch] = 0
            tSize[ch] = 1 + tSize.get(ch, 0)

        left = 0
        right = 0
        minLeft = float('-inf')
        minRight = 0

        while(right < len(s)):
            currChar = s[right]
            # print('eval ', currChar, left, right)
            if(currChar not in tSize):
                if(not windowHasLetter):
                    left += 1
            else:
                windowHasLetter = True
                inWindow[currChar] += 1
                
                currLeftCh = s[left]
                # print(inWindow)
                while(left < right):
                    # print('currleft', left, currLeftCh)
                    if(currLeftCh not in tSize):
                        left += 1
                        currLeftCh = s[left]
                        continue
                    if(inWindow[currLeftCh] > tSize[currLeftCh]):
                        inWindow[currLeftCh] -= 1
                    else:
                        break
                    left += 1
                    currLeftCh = s[left]
                
                if(checkCompleteness() and (right - left) < (minRight - minLeft)):
                    minRight = right
                    minLeft = left

            right += 1
        
        if(minLeft == float('-inf')):
            return ""
        return s[minLeft:minRight+1]


