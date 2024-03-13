class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #Need to check if value is valid given a row, col
        n = 9
        def isValid(row, col, num):
            for i in range(9):
                if board[i][col] == num or board[row][i] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row + 1, 0)
            if board[row][col] == ".":
                for num in map(str, range(1, 10)):
                    if isValid(row, col, num):
                        board[row][col] = num
                        if solve(row, col+1):
                            return True
                        else:
                            board[row][col] = "."
                return False
            else:
                return solve(row, col + 1)
        solve(0,0)