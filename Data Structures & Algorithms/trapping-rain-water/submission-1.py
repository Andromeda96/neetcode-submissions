class Solution:
    def trap(self, height: List[int]) -> int:
        left =  0
        right = 1
        water_sum = 0
        l = len(height)
        for i in range(1, l-1):
            if max(height[0:i]) > height[i] and max(height[i+1:]) > height[i]:
                water_sum += min(max(height[0:i]), max(height[i+1:])) - height[i]

        return water_sum

