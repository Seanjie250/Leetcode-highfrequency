class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_ = defaultdict(list)
        for string in strs:
            list_[tuple(sorted(string))].append(string)
        return [item for _ , item in list_.items()]

        