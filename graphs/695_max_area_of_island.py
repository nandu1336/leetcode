from typing import List 

def max_area_of_island(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLUMNS = len(grid[0])
    visited = set()
    max_area = 0
    
    def bfs(i, j):
        if i < 0 or i >= ROWS or j < 0 or j >= COLUMNS or (i, j) in visited or grid[i][j] == 0:
            return 0 
        
        visited.add((i, j))
        res = 1
        res += bfs(i + 1, j)
        res += bfs(i - 1, j)
        res += bfs(i, j + 1)
        res += bfs(i, j - 1)

        return res
                
    for i in range(ROWS):
        for j in range(COLUMNS):
            if grid[i][j] == 1 and (i, j) not in visited:
                area = bfs(i, j)
                if area > max_area:
                    max_area = area
                    
    return max_area


if __name__ == "__main__":
    print(max_area_of_island(grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))