class Solution:
    def isValidSudoku(self, board) -> bool:
        res = set()
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    check_x = (element, f'Row {i}')
                    check_y = (element, f'Col {j}')
                    check_total = (element, i//3, j//3)
                    if check_x in res or check_y in res or check_total in res:
                        return False
                    
                    res.add(check_x)
                    res.add(check_y)
                    res.add(check_total)
        return True
