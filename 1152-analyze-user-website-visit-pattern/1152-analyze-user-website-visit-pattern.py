class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        logs = sorted(zip(timestamp , username , website))
        
        user_web = defaultdict(list)
        for t , u , w in logs:
            user_web[u].append(w)
        
        tuple_count = Counter()

        for u , w in user_web.items():
            if len(w) < 3:
                continue
            
            pattern_type = set(combinations(w , 3))

            for tuples in pattern_type:
                tuple_count[tuples] += 1


        best_score = -1
        best_pattern = None
        for tuple_ , count in tuple_count.items():
            if count > best_score or (count == best_score and tuple_ < best_pattern):
                best_score = count
                best_pattern = tuple_
                print(best_score)
                print(best_pattern)
        
        return best_pattern
            
        
                




        