class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_seen = set()
            col_seen = set()
            box_seen = set()
            for j in range(9):
                # Row check
                if board[i][j] != "." :
                    if board[i][j] in row_seen: return False
                    row_seen.add(board[i][j])
                
                # Column check
                if board[j][i] != "." :
                    if board[j][i] in col_seen: return False
                    col_seen.add(board[j][i])
                
                # 3x3 Box check
                # Logic: iterate through all 9 boxes using 'i' and 9 cells using 'j'
                row_idx = 3 * (i // 3) + (j // 3)
                col_idx = 3 * (i % 3) + (j % 3)
                box_element = board[row_idx][col_idx]
                if box_element != ".":
                    if box_element in box_seen: return False
                    box_seen.add(box_element)
                    
        return True
