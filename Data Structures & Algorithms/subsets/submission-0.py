class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        idx = 0 
        res = []

        def backtrack(idx,arr):
            if idx == len(nums):
                res.append(arr.copy())
                return
            
            arr.append(nums[idx])
            backtrack(idx+1,arr)
            arr.pop()
            backtrack(idx+1,arr)

        backtrack(0,[])
        return res


        