class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS,COLS = len(grid),len(grid[0])

        def dfs(row,col,area):
            if row<0 or col<0 or row>=ROWS or col>=COLS or grid[row][col] == 0:
                return area
            
            grid[row][col] = 0
            area+=1

            area = dfs(row+1,col,area)
            area = dfs(row-1,col,area)
            area = dfs(row,col-1,area)
            area = dfs(row,col+1,area)
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea=max(maxArea,dfs(r,c,0))
        
        return maxArea