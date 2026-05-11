class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            col = set()
            box = set()

            for j in range(9):

                if board[i][j] != ".":
                    if board[i][j] in row: 
                        return False
                    row.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
            
                row_idx = 3 * (i//3) + (j//3)
                col_idx = 3 * (i%3) + (j%3)

                if board[row_idx][col_idx] != ".":
                    if board[row_idx][col_idx] in box:
                        return False
                    box.add(board[row_idx][col_idx])
        
        return True