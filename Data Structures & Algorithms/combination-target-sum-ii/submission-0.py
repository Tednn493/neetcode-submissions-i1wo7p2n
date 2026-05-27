class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()

        def backtrack(idx,path,total):
            if total == target:
                res.append(list.copy(path))
                return
            
            if idx == len(candidates) or total>target:
                return
            
            path.append(candidates[idx])
            backtrack(idx+1,path,total+candidates[idx])
            path.pop()
            
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(idx+1,path,total)
        
        backtrack(0,[],0)
        return res
        