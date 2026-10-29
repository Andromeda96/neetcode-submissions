class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        s = numbers[l] + numbers[r]
        while s != target:
            if s < target:
                l = l + 1
            else:
                r = r - 1
            s = numbers[l] + numbers[r]

        return [l + 1, r + 1]