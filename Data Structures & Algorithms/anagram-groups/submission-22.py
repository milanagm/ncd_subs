class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouper = {}
        for i in strs: 
            s_i = tuple(sorted(i))
            if s_i in grouper: 
                grouper[s_i].append(i)
            else: 
                grouper[s_i] = []
                grouper[s_i].append(i)


        return list(grouper.values())
            
        