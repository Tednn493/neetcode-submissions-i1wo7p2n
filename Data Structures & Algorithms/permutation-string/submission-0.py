import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r=0,len(s1)
        charCount = {}

        for char in s1:
            if char in charCount.keys():
                charCount[char]+=1
            else:
                charCount[char]=1
        
        def subPerm (string,charCount):
            charCount = copy.deepcopy(charCount)
            for char in string:
                if char not in charCount.keys():
                    return False
                elif charCount[char]==0:
                    return False
                else:
                    charCount[char]-=1
            
            for key in charCount.keys():
                if charCount[char] != 0:
                    return False
            return True

        while r <=len(s2):
            if subPerm(s2[l:r],charCount):
                return True
            else:
                l+=1
                r+=1
            
        return False





        