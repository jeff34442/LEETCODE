class Solution:
    def countBits(self, n: int):
        output_array = [0,1]

        if n == 0:
            return [0]
        if n == 1:
            return output_array
        
        for i in range(2, n+1):
            #take the i and convert to bits
            binary_rep = len(bin(i)[2:].replace('0', ''))
            output_array.append(binary_rep)
        return output_array