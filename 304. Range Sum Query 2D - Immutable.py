class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.sums = [[0] * (len(matrix and matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.sums[i + 1][j + 1] = self.sums[i][j + 1] + self.sums[i + 1][j] - self.sums[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][
            col1]

    