class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for pt in s:
            if pt == '[' or pt == '(' or pt == '{':
                stack.append(pt)
            else:
                if(len(stack)) == 0:
                    return False
                stackEnd = stack[len(stack)-1]
                if pt == ']' and stackEnd == '[':
                    stack.pop()
                elif pt == ')' and stackEnd == '(':
                    stack.pop()
                elif pt == '}' and stackEnd == '{':
                    stack.pop()
                else:
                    return False
        if(len(stack) != 0):
            return False
        return True