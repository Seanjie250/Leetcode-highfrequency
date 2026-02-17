class Solution:
    def add_one(self, cur, i):
        cur = list(cur)
        if cur[i] == '9':
            cur[i] = '0'
        else:
            cur[i] = chr(ord(cur[i]) + 1)
        return ''.join(cur)
    def minus_one(self, cur, i):
        cur = list(cur)
        if cur[i] == '0':
            cur[i] = '9'
        else:
            cur[i] = chr(ord(cur[i]) - 1)
        return ''.join(cur)

    def neighbours(self, cur):
        nei = []
        for i in range(4):
            nei.append(self.add_one(cur , i))
            nei.append(self.minus_one(cur , i))
        return nei
                
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        start = "0000"
        if start in deadends:
            return -1
        q.append("0000")
        visited = set()
        dead = set(deadends)
        step = 0
        while q:
            for i in range(len(q)):
                cur = q.popleft()
               
                if cur == target:
                    return step
                for nei in self.neighbours(cur):
                    if nei not in visited and nei not in dead:
                        q.append(nei)
                        visited.add(nei)

            step +=1
        return - 1


