from typing import List 

def exist(board: List[List[str]], word: str) -> bool:
    visited = set()
    ROWS = len(board)
    COLUMNS = len(board[0])

    def dfs(i, j, char_index):
        if i < 0 or i >= ROWS or j < 0 or j >= COLUMNS or (i, j) in visited: return False 
        if board[i][j] != word[char_index]: return False
        
        if char_index == len(word) - 1: return True

        visited.add((i, j))
        result = (  dfs(i + 1, j, char_index + 1) or dfs(i, j + 1, char_index + 1) or
                    dfs(i - 1, j, char_index + 1) or dfs(i, j - 1, char_index + 1))
        
        visited.remove((i, j))
        return result

    
    for i in range(ROWS):
        for j in range(COLUMNS):
            if board[i][j] == word[0]:
                if dfs(i, j, 0): return True

    return False
if __name__ == "__main__":
    print(exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED"))
    print(exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="SEE"))
    print(exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCB"))
    print(exist(board=[["a","b"],["c","d"]], word="bacd"))