# Last updated: 5/20/2025, 4:30:24 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_index = defaultdict(int)
        for num in nums:
            value_index[num] += 1
        time_index = defaultdict(list)
        for key in value_index:
            time_index[value_index[key]].append(key)
        key = list(time_index.keys())
        key.sort()
        result = []
        count = 0
        while key and count != k:
            result += time_index[key[-1]]
            count += 1
            key.pop()
        return result[0:k]
 
        
        