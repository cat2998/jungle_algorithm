class Solution:
    def bfs(self, grid: List[List[str]], i, j):
        que = deque()
        m = len(grid)
        n = len(grid[0])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        que.append((i, j))
        grid[i][j] = '2'
        while que:
            x, y = que.popleft()
            for _x, _y in zip(dx, dy):
                if (0 <= x + _x < m and 0 <= y + _y < n and grid[x + _x][y + _y] == '1'):
                    que.append((x + _x, y + _y))
                    grid[x + _x][y + _y] = '2'
    
    def dfs(self, grid: List[List[str]], i, j):
        m = len(grid)
        n = len(grid[0])
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        grid[i][j] = '2'
        for x, y in zip(dx, dy):
            if (0 <= i + x < m and 0 <= j + y < n and grid[i + x][j + y] == '1'):
                grid[i + x][j + y] = '2'
                self.dfs(grid, i + x, j + y)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # self.bfs(grid, i, j)
                    self.dfs(grid, i, j)
                    answer += 1
        return answer
