class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        triples = []
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:    
                ts = nums[i] + nums[l] + nums[r]
                if ts < 0:
                    l += 1
                elif ts > 0:
                    r = r - 1
                else:
                    triple = [nums[i], nums[l], nums[r]]
                    if triple not in triples:
                        triples.append(triple)
                    l += 1
                    r -= 1

        return triples