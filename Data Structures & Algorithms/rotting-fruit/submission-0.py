class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS= len(grid),len(grid[0])
        fresh = 0
        q=deque()

        def addRoom(r,c):
            nonlocal fresh
            if (r<0 or r>=ROWS or c<0 or c>=COLS or grid[r][c]==0 or grid[r][c] == 2):
                return
            grid[r][c] = 2
            fresh -= 1
            q.append([r,c])



        for r in range (ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh+=1
        
        t=0
        while q and fresh > 0:
            for i in range (len(q)):
                r,c=q.popleft()

                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            t+=1

        if fresh > 0:
            return -1
        else:
            return t

        