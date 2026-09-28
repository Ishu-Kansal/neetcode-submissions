class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        freq = 0
        left = 0
        maxLen = 0
        for i in range(len(s)):
            counts[ord(s[i]) - ord('A')] += 1
            freq = max(freq, counts[ord(s[i]) - ord('A')])
            while((i - left + 1) - freq > k):
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            maxLen = max(maxLen, i - left + 1)

        return maxLen


