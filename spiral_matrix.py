class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0 for i in range(n)] for j in range(n)]
        if n == 1:
            matrix[0][0] = 1
            return matrix
        row = 0
        col = 0
        count = 1
        while n > 0:
            if n == 1:
                matrix[row][col] = count
                break
            # Fill right 
            for k in range(n - 1):
                matrix[row][col] = count
                col += 1
                count += 1
            # Fill down 
            for k in range(n - 1):
                matrix[row][col] = count
                row += 1
                count += 1
            # Fill left 
            for k in range(n - 1):
                matrix[row][col] = count
                col -= 1
                count += 1
            # Fill up
            for k in range(n - 1):
                matrix[row][col] = count
                row -= 1
                count += 1
            row += 1
            col += 1
            n -= 2
        return matrix

n=int(input("Enter the n value : "))
s = Solution()
res= s.generateMatrix(n)
print(res)
