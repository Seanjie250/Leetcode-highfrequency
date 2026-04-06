class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        for string in strs:
            counter[tuple(sorted(string))].append(string)
        print(counter)
        rst = []
        for index , sublist in counter.items():
            rst.append(sublist)
        return rst

        