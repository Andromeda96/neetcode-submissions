class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_rest = []
        for i in range(len(nums)):
            nums_rest.append(target - nums[i])

        for i in range(len(nums)):
            if nums_rest[i] in nums:
                l = [nums.index(nums_rest[i]), i]

        return l