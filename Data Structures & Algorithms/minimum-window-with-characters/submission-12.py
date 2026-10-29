class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        wCount = {}
        tCount = {}

        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1


        have, need = 0, len(tCount)
        res, resLen = [-1, -1], len(s) + 1
        l = 0
        for r in range(len(s)):
            c = s[r]
            wCount[c] = wCount.get(c, 0) + 1
            if c in tCount and wCount[c] == tCount[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                wCount[s[l]] -= 1
                if s[l] in tCount and wCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r+ 1] if resLen <= len(s) else ''