class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collect = defaultdict(list)
        for s in strs:
            collect[tuple(sorted(s))].append(s)
        return list(collect.values())

        