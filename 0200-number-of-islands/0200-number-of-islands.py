class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        out=0

        def dfs(i,j):
            grid[i][j]=0
            for dx,dy in dir:
                x=i+dx
                y=j+dy
                if 0<=x<n and 0<=y<m and grid[x][y]=='1':
                    dfs(x,y)

        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    out+=1
                    dfs(i,j)
        return out