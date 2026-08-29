class Solution:
    def minWindow(self, s: str, t: str) -> str:
        inWindow = {}
        tSize = {}

        for ch in t:
            inWindow[ch] = 0
            tSize[ch] = 1 + tSize.get(ch, 0)

        # 'need' is total unique characters required
        # 'have' is how many unique characters currently meet or exceed target frequency
        need = len(tSize)
        have = 0

        left = 0
        right = 0
        minLeft = float('-inf')
        minRight = 0

        while right < len(s):
            currChar = s[right]
            
            if currChar in tSize:
                inWindow[currChar] += 1
                # If adding this character fulfills its required frequency
                if inWindow[currChar] == tSize[currChar]:
                    have += 1
                
                currLeftCh = s[left]
                
                while left < right:
                    if currLeftCh not in tSize:
                        left += 1
                        currLeftCh = s[left]
                        continue
                    
                    if inWindow[currLeftCh] > tSize[currLeftCh]:
                        inWindow[currLeftCh] -= 1
                        left += 1
                        currLeftCh = s[left]
                    else:
                        break

                # Replaced helper function with O(1) counter check
                if have == need and (right - left) < (minRight - minLeft):
                    minRight = right
                    minLeft = left

            right += 1
        
        if minLeft == float('-inf'):
            return ""
        return s[minLeft:minRight+1]