"""
示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'}': '{', ']': '[', ')': '('}
        stack = []
        for ch in s:
            if ch in dict:
                if not stack or stack[-1] != dict[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return True


if __name__ == '__main__':
    s = "(]"
    solution = Solution()
    print(solution.isValid(s))  # 'true