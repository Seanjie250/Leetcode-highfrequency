class Solution:
    def find(self,u,parents):
        if parents[u] != u:
            parents[u] = self.find(parents[u],parents)
        return parents[u]
    def union(self,u,v,parents):
        root_u = self.find(u,parents)
        root_v = self.find(v,parents)
        if root_u != root_v:
            parents[root_v] = root_u 


        
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        
        for u,v in edges:
            self.union(u,v,parents)

        groups = defaultdict(set)
        for i in range(n):
            root = self.find(i,parents)
            groups[root].add(i)
        
        edge_count = defaultdict(int)
        for u,v in edges:
            root = self.find(u,parents)
            edge_count[root] += 1

        count = 0
        for root,nodes in groups.items():
            size = len(nodes)
            expected = ( size * (size - 1) )// 2
            if expected == edge_count[root]:
                count += 1

        return count






        