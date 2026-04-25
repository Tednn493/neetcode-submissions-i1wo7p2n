class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        tH=0
        if h == len(piles):
            return r
        
        while l<=r:
            tH=0
            k = (l+r) // 2
            for p in piles:
                tH += math.ceil(float(p) / k)
            if tH <= h:
                res = k
                r = k-1
            else: 
                l = k+1
        return res

        

        