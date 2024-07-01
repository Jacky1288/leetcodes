class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in dic:
                if not stack or stack[-1] != dic[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack