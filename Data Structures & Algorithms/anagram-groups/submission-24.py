class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for s in strs: 
            s_s = tuple(sorted(s))
            if s_s in grouped: 
                grouped[s_s].append(s)
            else: 
                grouped[s_s] = []
                grouped[s_s].append(s)
        return list(grouped.values())

              
        