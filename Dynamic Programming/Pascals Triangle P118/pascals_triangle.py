class Solution:
    def generate(self, numRows: int):

        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        get_rows = self.generate(numRows - 1)
        previous_row = get_rows[-1]
        current_row = [1]
        for i in range(1, numRows - 1):
            current_row.append(previous_row[i-1] + previous_row[i])
        
        current_row.append(1)
        get_rows.append(current_row)
        return get_rows