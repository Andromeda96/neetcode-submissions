class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sort_nums = sorted(nums)
        max_l = 1
        current_l = 1
        prev = sort_nums[0]
        for i in range(1, len(nums)):
            if sort_nums[i] == prev + 1:
                current_l += 1
                if current_l > max_l:
                    max_l = current_l
            elif sort_nums[i] == prev:
                pass
            else:
                current_l = 1
            prev = sort_nums[i]

        return max_l
            