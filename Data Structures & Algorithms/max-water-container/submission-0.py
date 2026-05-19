class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        i, j = 0, len(heights) - 1
        while i < j:
            if (j - i)*min(heights[i], heights[j]) > max:
                max = (j - i)*min(heights[i], heights[j])
            if (heights[i] < heights[j]):
                i += 1
            else:
                j -= 1
        return max
                
            

        