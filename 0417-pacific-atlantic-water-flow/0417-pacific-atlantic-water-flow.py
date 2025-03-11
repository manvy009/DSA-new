class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = [[False] * cols for _ in range(rows)]
        atlantic_reachable = [[False] * cols for _ in range(rows)]

        def dfs(r, c, reachable):
            # Mark the current cell as reachable
            reachable[r][c] = True
            # Explore all four directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Check if the neighbor is within bounds and not already reachable
                if 0 <= nr < rows and 0 <= nc < cols and not reachable[nr][nc]:
                    # Check if water can flow from the neighbor to the current cell
                    if heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable)

        # Start DFS from the Pacific Ocean (top and left edges)
        for r in range(rows):
            dfs(r, 0, pacific_reachable)  # Left edge
        for c in range(cols):
            dfs(0, c, pacific_reachable)  # Top edge

        # Start DFS from the Atlantic Ocean (bottom and right edges)
        for r in range(rows):
            dfs(r, cols - 1, atlantic_reachable)  # Right edge
        for c in range(cols):
            dfs(rows - 1, c, atlantic_reachable)  # Bottom edge

        # Find cells that can reach both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])
        return result