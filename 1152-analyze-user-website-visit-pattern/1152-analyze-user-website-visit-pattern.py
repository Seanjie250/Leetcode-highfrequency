class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        logs = sorted(zip(timestamp , username , website))
        
        users_site = defaultdict(list)
        for t, u , w in logs:
            users_site[u].append(w)

        pattern_user = Counter()  
        for u , w in users_site.items():
            if len(w) < 3:
                continue
            
            pattern_ = set(combinations(w, 3))

            for tuple_ in pattern_:
                pattern_user[tuple_] += 1

        best_score = 0
        best_pattern = None
        for tuple_  , count in pattern_user.items():
            if count > best_score or (tuple_ < best_pattern and best_score == count):
                best_score = count
                best_pattern = tuple_
        
        return best_pattern 






        