class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        for l in range(len(heights)):
            r = len(heights)-1
            while l<r:
                h = min(heights[l],heights[r])
                w = r-l
                vol = max(vol,h*w)
                r=r-1
        return vol


        