"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        rowStart = 0
        rowEnd = len(matrix)-1
        colStart = 0
        colEnd = len(matrix[0])-1
        res=[]
        while (rowStart<=rowEnd and colStart<=colEnd):
            for i in range(colStart,colEnd+1,1):
                res.append(matrix[rowStart][i])
                print("1")
            for i in range(rowStart+1,rowEnd+1,1):
                res.append(matrix[i][colEnd])
                print("2")
            if rowEnd>rowStart:
                for i in range(colEnd-1,colStart,-1):
                    res.append(matrix[rowEnd][i])
                    print("3")
            if colEnd>colStart:
                for i in range(rowEnd,rowStart,-1):
                    res.append(matrix[i][colStart])
                    print("4")
            rowStart=rowStart+1
            colStart=colStart+1
            rowEnd-=1
            colEnd-=1
        return res