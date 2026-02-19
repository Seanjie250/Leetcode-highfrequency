class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect = defaultdict(list)
        for string in strs:
            collect[tuple(sorted(string))].append(string)
        return list(collect.values())

        