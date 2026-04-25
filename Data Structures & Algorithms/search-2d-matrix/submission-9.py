class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix)-1

        if matrix[0][0] > target:
            return False
        
        if matrix[-1][-1] < target:
            return False
        
        while l<=r:
            m = (l+r) // 2
            if matrix[m][0]<=target and matrix[m][-1] >= target:
                arr = matrix[m]
                break
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                r = m - 1
        else:
            return False
            
        if not arr:
            return false

        l = 0 
        r = len(arr) - 1

        while l<=r:
            m = (l+r) // 2
            if arr[m] == target:
                return True
            elif arr[m]<target:
                l = m + 1
            else: 
                r = m - 1
        return False
        
                



        