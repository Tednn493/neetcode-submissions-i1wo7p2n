class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,1
        maxlen = 1
        if not s:
            return 0
        chars = {s[0]:0}

        while r < len(s):
            if s[r] not in chars or chars[s[r]] < l:
                chars[s[r]] = r
                r+=1
                maxlen = max(r-l,maxlen)
            else:
                l = chars[s[r]] + 1
                chars[s[r]] = r
                r+=1
        return maxlen

                


        