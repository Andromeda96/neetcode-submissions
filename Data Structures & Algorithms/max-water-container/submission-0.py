class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        n = len(heights)
        for i in range(n-1):
            for j in range(i, n):
                if min(heights[i], heights[j])*(j - i) > m:
                    m = min(heights[i], heights[j])*(j - i)

        return m