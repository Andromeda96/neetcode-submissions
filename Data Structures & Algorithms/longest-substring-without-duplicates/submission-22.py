class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_dict = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            ch = s[r]

            if ch in prev_dict and prev_dict[ch] >= l:
                l = prev_dict[ch] + 1
            
            max_len = max(r - l + 1, max_len)
            prev_dict[ch] = r

        return max_len