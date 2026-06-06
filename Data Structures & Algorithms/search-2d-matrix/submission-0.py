class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row, col = len(matrix), len(matrix[0])

        i, j = 0, col - 1

        while i < row and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        
        return False