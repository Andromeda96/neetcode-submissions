class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sort_nums = sorted(nums)
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        topK = sorted(counts.items(), key = lambda x: -x[1])
        l = []
        for i in range(k):
            l.append(topK[i][0])

        return l