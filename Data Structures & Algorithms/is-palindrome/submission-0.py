class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        s = s.lower()
        while(i < j):
            i_ch = s[i]
            j_ch = s[j]
            if(not i_ch.isalnum()):
                i+=1
                continue
            if(not j_ch.isalnum()):
                j-=1
                continue
            if(i_ch != j_ch):
                return False
            i+=1
            j-=1
        return True