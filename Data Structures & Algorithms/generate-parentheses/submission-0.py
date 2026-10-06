class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        base = "("
        arr = [
            {
                "s": base,
                "open": 1,
                "close": 0
            }
        ]

        res = []

        while(len(arr) > 0):
            currObj = arr.pop()
            if(currObj["open"] < n):
                newStr = currObj["s"] + "("
                arr.append({"s": newStr, "open": currObj["open"] + 1, "close": currObj["close"]})
            if(currObj["close"] < currObj["open"]):
                arr.append({"s": currObj["s"] + ")", "open": currObj["open"], "close": currObj["close"] + 1})
            if(currObj["open"] == n and currObj["close"] == n):
                res.append(currObj["s"])
        
        return res