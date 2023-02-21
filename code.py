class Solution(object):
    def searchMatrix(self, matrix, target):
        i, j = 0, -1
        while i<len(matrix) and j >= -len(matrix[0]) and matrix[i][j] != target:
            if matrix[i][j] > target:
                j-= 1
            else:
                i+=1
        return True if i<len(matrix) and j >= -len(matrix[0]) else False

     
       
