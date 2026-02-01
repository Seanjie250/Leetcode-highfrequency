class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def id_to_rc(s:int) -> tuple(int , int):
            q , r  = divmod(s - 1 , n)
            row = n - q - 1
            if q % 2 == 0:
                col = r
            elif q % 2 == 1:
                col = n - r - 1
            return row , col
        
        target = n * n 
        dist = [-1] * (target + 1)
        dist[1] = 0
        q = deque([1])

        while q:
            cur = q.popleft()
            if cur == target:
                return dist[cur]
            for nxt in range(cur + 1 , min(target , cur + 6) + 1):
                r , c = id_to_rc(nxt)
                dest = board[r][c] if board[r][c] != -1 else nxt
                if dist[dest] == -1:
                    dist[dest] = dist[cur] + 1
                    q.append(dest)
        return -1

        
        


        