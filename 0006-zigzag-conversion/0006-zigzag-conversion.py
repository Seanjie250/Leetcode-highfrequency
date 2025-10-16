class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        store = [[''] * (len(s)) for _ in range(numRows)]
        s = deque(s)
        i = 0
        row = 0
        down = True
        while s:
            store[row][i] = s.popleft()
            if down:
                row += 1
            else:
                row -= 1 
            if row == 0:
                down = True
            elif row == numRows - 1:
                down = False
            i += 1

        rst = ''
        for r in store:
            rst += "".join(r)

        return rst

        


            

        


            
            
    
        
           


        