class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        t = 10000000
        min_k = 0
        while l <= r:
            k = (l + r) // 2
            t = sum([math.ceil(x/k) for x in piles])
            if t <= h:
                res = k
                r = k - 1
            elif t > h:
                l = k + 1
        
        return res
