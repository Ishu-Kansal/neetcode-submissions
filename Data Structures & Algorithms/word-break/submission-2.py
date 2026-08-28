class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        isWord = {}

        def dfs(currStr) -> bool:
            if(currStr in isWord):
                return isWord[currStr]
            currIsWord = False
            for word in wordDict:
                if(currStr == word):
                    isWord[currStr] = True
                    return True
                if(currStr[:len(word)] == word):
                    currIsWord = currIsWord or dfs(currStr[len(word):])
            
            isWord[currStr] = currIsWord
            return currIsWord
        
        return dfs(s)
