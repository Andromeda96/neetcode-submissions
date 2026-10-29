class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_dict = {}
        l = 0
        max_len = 0

        for r in range(len(s)):
            ch = s[r]

            # A previous occurrence matters only if it is
            # inside the current window.
            if ch in prev_dict and prev_dict[ch] >= l:
                l = prev_dict[ch] + 1

            # Store the character's latest absolute index.
            prev_dict[ch] = r

            max_len = max(max_len, r - l + 1)

        return max_len