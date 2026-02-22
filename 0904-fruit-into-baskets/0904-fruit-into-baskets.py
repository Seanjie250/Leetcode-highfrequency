class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked = defaultdict(int)
        left   = 0 
        maxm = float('-inf')
        for x , right in enumerate(fruits):
            picked[right] += 1
            while len(picked) > 2:
                picked[fruits[left]] -= 1
                if picked[fruits[left]] == 0:
                    del picked[fruits[left]]
                left += 1
            maxm = max(maxm  , x - left + 1)


        return maxm
                
                


        