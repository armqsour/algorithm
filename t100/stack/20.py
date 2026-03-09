class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        s = list(s)
        for c in s:
            if stack:
                if (stack[-1], c) in (('(', ')'), ('[', ']'), ('{', '}')):
                    stack.pop()
                    continue
            stack.append(c)
        return not stack