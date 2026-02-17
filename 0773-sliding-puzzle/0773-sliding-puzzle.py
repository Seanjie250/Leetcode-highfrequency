class Solution:
    def swap(self, cur , i , j):
        chars = list(cur)
        chars[i]  , chars[j] = chars[j] , chars[i]
        return ''.join(chars)
    def neighbours(self,cur):
        neighbour_s = [
            [1 , 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]
        neighbours_ = []
        index = cur.index('0')
        for n in neighbour_s[index]:
            ans = self.swap(cur , index , n)
            neighbours_.append(ans)
        return neighbours_
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m , n = len(board) , len(board[0])
        ans = '123450'
        start = ''
        for i in range(m):
            for j in range(n):
                start += str(board[i][j])
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)
        step = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                print(cur)
                if cur == ans:
                    return step
                for neighbour in self.neighbours(cur):
                    if neighbour not in visited:
                        q.append(neighbour)
                        visited.add(neighbour)
                print(visited)
            
            step +=1
        return -1

                



        