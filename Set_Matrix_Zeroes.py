# Leetcode: https://leetcode.com/problems/set-matrix-zeroes/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # m = len(matrix)
        # n = len(matrix[0])
        a = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    a.append([i,j])
        for i,j in a:
            for r in range(len(matrix[0])):
                matrix[i][r] = 0
            for c in range(len(matrix)):
                matrix[c][j] = 0
