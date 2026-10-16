class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouper = defaultdict(list())
        for i in strs: 
            s_i = sorted(i)
            grouper[s_i].append(i)
        grouper_v = []
        for i in grouper: 
            grouper_v.append(grouper[i])
        return grouper_v
            
        