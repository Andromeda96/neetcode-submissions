class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        n = len(heights)
        m = min(heights[0], heights[-1])*(n-1)
        l = 0
        r = n-1
        while l != r:
            if heights[l] > heights[r]:
                r = r - 1
            elif heights[l] < heights[r]:
                l = l + 1
            else:
                l = l + 1
            area = (r - l)*min(heights[l], heights[r])
            if area > m:
                m = area

        return m



        return m