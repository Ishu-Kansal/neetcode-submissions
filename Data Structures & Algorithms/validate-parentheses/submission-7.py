class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            ch = s[i]
            if(ch == '[' or ch == '(' or ch == '{'):
                stack.append(ch)
            else:
                if(len(stack) == 0):
                    return False
                if(ch == ']' and stack[-1] != '['):
                    return False
                if(ch == '}' and stack[-1] != '{'):
                    return False
                if(ch == ')' and stack[-1] != '('):
                    return False
                stack.pop()
        
        return (len(stack) == 0)