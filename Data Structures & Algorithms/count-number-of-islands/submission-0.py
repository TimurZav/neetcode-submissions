class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
          return 0

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(r, c):
            """BFS от клетки (r, c) - помечает весь остров"""
            queue = deque([(r, c)])
            grid[r][c] = "0"  # помечаем как посещенную

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # если в границах и это земля
                    if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "1":
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = "0"  # помечаем

        # Главный цикл
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1  # нашли новый остров!
                    bfs(row, col)  # помечаем весь остров

        return islands