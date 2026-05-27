class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        def bt(idx,path):
            if idx == len(nums):
                res.append(path.copy())
                return

            path.append(nums[idx])
            bt(idx+1,path)
            path.pop()
            
            while idx < len(nums)-1 and nums[idx] == nums[idx+1]:
                idx+=1
            bt(idx+1,path)
        
        bt(0,[])
        return res
            
        