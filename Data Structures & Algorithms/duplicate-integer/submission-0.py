class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        unique_nums = []
        for i in nums:
            if i in unique_nums:
                flag = True
            else:
                unique_nums.append(i)
        return flag