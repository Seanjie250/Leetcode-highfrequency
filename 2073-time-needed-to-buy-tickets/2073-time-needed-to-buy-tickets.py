class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        count = 0
        for index , ticket in enumerate(tickets):
            q.append((index , ticket))
        while q:
            index , ticket = q.popleft()
            if ticket - 1 == 0 and index == k:
                return count + 1
            elif ticket - 1 > 0:
                q.append((index , ticket - 1))
                count += 1
            elif ticket - 1 == 0 and index != k:
                count += 1
        
        