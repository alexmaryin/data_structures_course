class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        max_len = 0
        temp = {}
        while i < len(s):
            while j < len(s) and s[j] not in temp:
                temp[s[j]] = 1
                j += 1
            max_len = max(max_len, len(temp))
            temp.clear()
            i += 1
            j = i
        return max_len


if __name__ == '__main__':
    inp = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(inp))
