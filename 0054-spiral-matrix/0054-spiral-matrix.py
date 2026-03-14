class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m , n = len(matrix) , len(matrix[0])
        rst = []
        l_b , r_b , t_b , b_b = 0 , n - 1 , 0 , m - 1
       
        while l_b <= r_b and t_b <= b_b:
            for i in range(l_b ,r_b + 1):
                rst.append(matrix[t_b][i])
            t_b += 1
            for i in range(t_b , b_b + 1):
                rst.append(matrix[i][r_b])
            r_b -= 1
            if t_b <= b_b:
                for i in range(r_b ,l_b - 1, - 1):
                    rst.append(matrix[b_b][i])
                b_b -= 1
            if l_b <= r_b:
                for i in range(b_b , t_b - 1 , - 1):
                    rst.append(matrix[i][l_b])
                l_b += 1
        return rst
        
        