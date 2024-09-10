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

    def lengthOfLongestSubstring2(self, s: str) -> int:
        length = len(s) # 长度
        maxlen = 0
        substr = set()
        for i in range(length-1):
            if i == 0:
                substr.add(s[i])
            else:
                substr.remove(s[i-1])
                substr.add(s[i])
            for j in range(i+1, length):
                if s[j] in substr:
                    break
                substr.add(s[j])
            maxlen = max(maxlen, len(substr))

        return maxlen


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring2('abcabcbb'))