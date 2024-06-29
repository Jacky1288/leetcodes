class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # s = "abcabcbb"
        length = len(s)
        occ = set()
        rk, ans = -1, 0
        for i in range(length):
            if i != 0:
                occ.remove(s[i-1])
            while rk+1 < length and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, rk + 1 - i)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbb'))