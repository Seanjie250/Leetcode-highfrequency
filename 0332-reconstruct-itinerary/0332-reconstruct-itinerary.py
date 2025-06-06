from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        target = defaultdict(list)
        for ticket in tickets:
            target[ticket[0]].append(ticket[1]) #store tickets information
        for key in target:
            target[key].sort(reverse = True) #sort with lexical order
        rst = []
        self.backtracking("JFK",tickets,target,rst)
        return rst[::-1]

    def backtracking(self,airport,tickets,targets,rst):
        while targets[airport]:
            next_airport = targets[airport].pop()
            self.backtracking(next_airport,tickets,targets,rst)
        rst.append(airport)
        
        
        


