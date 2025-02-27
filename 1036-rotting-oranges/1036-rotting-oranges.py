class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        q=deque()
        cnt=0
        for r in range(rows):
            for c in range (cols):
                if grid[r][c]==2:
                    q.append((r,c,0))
                elif grid[r][c]==1:
                    cnt+=1
        time=0
        while q:
            row,col,mins=q.popleft()
            for dr,dc in dirs:
                newR,newC=row+dr, col+dc
                if 0<=newR<rows and 0<=newC<cols and grid[newR][newC]==1:
                    grid[newR][newC]=2
                    cnt-=1
                    q.append((newR,newC,mins+1))
                    time=mins+1
        return time if cnt==0 else -1