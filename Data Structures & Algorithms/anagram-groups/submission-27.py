class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouper = {}
        for i in strs: 
            i_s = "".join(sorted(i))
            grouper.setdefault(i_s, []).append(i) 

        return list(grouper.values())


    
        
        