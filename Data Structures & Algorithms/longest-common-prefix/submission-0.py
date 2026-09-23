class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def calcSimilarity(word1, word2):
            sim = ""
            for i in range(min(len(word1), len(word2))):
                if(word1[i] == word2[i]):
                    sim += word1[i]
                else:
                    break
            return sim

        runningPrefix = strs[0]
        for word in strs:
            runningPrefix = calcSimilarity(runningPrefix, word)

        return runningPrefix