class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) == 0):
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            '5': "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = list(mapping[digits[0]])
        for digit in digits[1:]:
            
            intermediate = []
            for s in res:
                for ch in mapping[digit]:
                    intermediate.append(s + ch)
            res = intermediate.copy()

        return res
        