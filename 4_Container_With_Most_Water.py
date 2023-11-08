class Solution(object):
    def maxArea(self, height):
        area = 0
        max_area = 0
        left = 0
        right = len(height)-1
        l=0
        b=0
        
        while left < right:
            b = min(height[left], height[right])
            l = right - left
            area = l*b
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        