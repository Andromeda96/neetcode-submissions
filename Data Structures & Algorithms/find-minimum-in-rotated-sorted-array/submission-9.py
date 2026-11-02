class Solution:
    def findMin(self, nums: List[int]) -> int:
        r = len(nums) - 1
        l = 0
        while l < r:
            m  = (r + l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1

        return nums[l]
