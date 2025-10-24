class Solution:
    def set_to_zero(self,matrix,row,col,x,y):
        for i in range(col):
            matrix[x][i] = 0
        for j in range(row):
            matrix[j][y] = 0
            
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        pos = []
        for i in range(col):
            for j in range(row):
                if matrix[j][i] != 0:
                    continue
                elif matrix[j][i] == 0:
                    pos.append([j,i])
        for j , i in pos:
            self.set_to_zero(matrix,row,col,j,i)

        
