class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouper = {}
        for i in strs: 
            i_s = i.sorted()
            grouper[grouper.get(i_s, 0)].append(i) # wie war hier die richtige syntax?

        return grouper.get_values()
        

    
        
        