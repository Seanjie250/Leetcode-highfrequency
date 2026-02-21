class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        logs = sorted(zip(timestamp , username , website))

        pattern = defaultdict(list)

        for t , u , w in logs:
            pattern[u].append(w)
        tuple_count = Counter()
        for u,w in pattern.items():
            if len(w) < 3:
                continue
            tuple_type = set(combinations(w , 3))
            for tuple_ in tuple_type:
                tuple_count[tuple_] += 1
            
        best_score = -1
        best_pattern = None
        for tuple_ , count in tuple_count.items():
            if count > best_score or (best_score == count and tuple_ < best_pattern):
                best_score = count 
                best_pattern = tuple_
        return best_pattern
            

