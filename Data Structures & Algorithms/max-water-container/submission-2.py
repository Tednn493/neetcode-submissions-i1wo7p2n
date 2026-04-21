class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        l, r = 0, len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            vol = max(vol, h * w)

            # Move the pointer on the shorter side inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return vol


        