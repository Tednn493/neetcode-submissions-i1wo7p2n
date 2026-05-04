class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxLen = 0
        res = 0
        count={}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxLen = max(maxLen, count[s[r]])

            while (r-l+1) - maxLen > k:
                count[s[l]] -= 1 
                l+=1 
            res = max(res, r-l + 1)
        return res
                  