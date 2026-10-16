class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouper = defaultdict(list)
        for i in strs: 
            s_i = ""
            for j in sorted(i): 
                s_i += "j"

            grouper[s_i].append(i)
            s_i = ""

        grouper_v = []
        for i in grouper: 
            grouper_v.append(grouper[i])
        return grouper_v
            
        