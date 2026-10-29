class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = False
        l_s = len(s)
        l_t = len(t)
        dic_s = {}
        dic_t = {}
        if l_s == l_t:
            for i in range(l_s):
                s_i = s[i]
                t_i = t[i]
                if s_i in dic_s.keys():
                    dic_s[s_i] += 1
                else:
                    dic_s[s_i] = 0
                if t_i in dic_t.keys():
                    dic_t[t_i] += 1
                else:
                    dic_t[t_i] = 0
            if dic_s == dic_t:
                flag = True
        return flag
